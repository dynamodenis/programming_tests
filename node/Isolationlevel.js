const { sequelize, Account, Transaction: TransactionModel } = require('./models');
const { Transaction } = require('sequelize');

const { Transaction } = require('sequelize');

// Shared lock
const account = await Account.findByPk(accountId, {
  lock: Transaction.LOCK.SHARE,
  transaction: t
});

// Exclusive lock
const account = await Account.findByPk(accountId, {
  lock: Transaction.LOCK.UPDATE,
  transaction: t
});

class FinancialService {
  
  // Safe money transfer with exclusive locks
  async transferMoney(fromAccountId, toAccountId, amount) {
    const transaction = await sequelize.transaction({
      isolationLevel: Transaction.ISOLATION_LEVELS.READ_COMMITTED
    });

    try {
      // Lock accounts in consistent order to prevent deadlocks
      const accountIds = [fromAccountId, toAccountId].sort((a, b) => a - b);
      
      // Get accounts with exclusive locks
      const accounts = await Account.findAll({
        where: { id: accountIds },
        lock: Transaction.LOCK.UPDATE,
        transaction,
        order: [['id', 'ASC']] // Consistent ordering prevents deadlocks
      });

      const fromAccount = accounts.find(acc => acc.id === fromAccountId);
      const toAccount = accounts.find(acc => acc.id === toAccountId);

      if (!fromAccount || !toAccount) {
        throw new Error('Account not found');
      }

      // Business logic validation
      if (fromAccount.balance < amount) {
        throw new Error('Insufficient funds');
      }

      if (fromAccount.status !== 'ACTIVE' || toAccount.status !== 'ACTIVE') {
        throw new Error('Account not active');
      }

      // Update balances
      await fromAccount.update({
        balance: fromAccount.balance - amount,
        updated_at: new Date()
      }, { transaction });

      await toAccount.update({
        balance: toAccount.balance + amount,
        updated_at: new Date()
      }, { transaction });

      // Create transaction records
      await TransactionModel.bulkCreate([
        {
          account_id: fromAccountId,
          type: 'DEBIT',
          amount: amount,
          reference_id: `TXN_${Date.now()}`,
          description: `Transfer to account ${toAccountId}`
        },
        {
          account_id: toAccountId,
          type: 'CREDIT',
          amount: amount,
          reference_id: `TXN_${Date.now()}`,
          description: `Transfer from account ${fromAccountId}`
        }
      ], { transaction });

      await transaction.commit();
      
      return {
        status: 'SUCCESS',
        fromBalance: fromAccount.balance - amount,
        toBalance: toAccount.balance + amount,
        transactionId: `TXN_${Date.now()}`
      };

    } catch (error) {
      await transaction.rollback();
      throw error;
    }
  }

  // Batch salary processing with shared locks for reading
  async processSalaryBatch(employeeIds) {
    const transaction = await sequelize.transaction();

    try {
      // Read employee data with shared locks (multiple salary processors can read)
      const employees = await Employee.findAll({
        where: { id: employeeIds },
        include: [
          { model: Account, as: 'bankAccount' },
          { model: SalaryStructure, as: 'salary' }
        ],
        lock: Transaction.LOCK.SHARE,
        transaction
      });

      // Get company account with exclusive lock (only one salary process at a time)
      const companyAccount = await Account.findOne({
        where: { type: 'COMPANY', status: 'ACTIVE' },
        lock: Transaction.LOCK.UPDATE,
        transaction
      });

      const totalSalaryAmount = employees.reduce((sum, emp) => 
        sum + emp.salary.gross_amount, 0
      );

      if (companyAccount.balance < totalSalaryAmount) {
        throw new Error('Insufficient company funds for salary batch');
      }

      // Process each salary transfer
      const salaryPromises = employees.map(async (employee) => {
        // Individual account lock for each employee
        const employeeAccount = await Account.findByPk(
          employee.bankAccount.id,
          { lock: Transaction.LOCK.UPDATE, transaction }
        );

        await employeeAccount.update({
          balance: employeeAccount.balance + employee.salary.gross_amount
        }, { transaction });

        // Create salary transaction record
        return TransactionModel.create({
          account_id: employee.bankAccount.id,
          type: 'SALARY_CREDIT',
          amount: employee.salary.gross_amount,
          reference_id: `SAL_${employee.id}_${Date.now()}`,
          description: `Salary for ${employee.name}`,
          processed_by: 'SYSTEM'
        }, { transaction });
      });

      await Promise.all(salaryPromises);

      // Update company account
      await companyAccount.update({
        balance: companyAccount.balance - totalSalaryAmount
      }, { transaction });

      await transaction.commit();
      return { status: 'SUCCESS', processedCount: employees.length };

    } catch (error) {
      await transaction.rollback();
      throw error;
    }
  }

  // Account balance inquiry with shared lock
  async getAccountBalance(accountId, includeTransactions = false) {
    const transaction = await sequelize.transaction();

    try {
      // Shared lock - multiple balance inquiries can happen simultaneously
      const account = await Account.findByPk(accountId, {
        lock: Transaction.LOCK.SHARE,
        transaction,
        include: includeTransactions ? [
          {
            model: TransactionModel,
            as: 'transactions',
            limit: 10,
            order: [['created_at', 'DESC']]
          }
        ] : []
      });

      await transaction.commit();
      return account;

    } catch (error) {
      await transaction.rollback();
      throw error;
    }
  }

  // Optimistic locking for account updates
  async updateAccountWithOptimisticLock(accountId, updates) {
    const maxRetries = 3;
    let retries = 0;

    while (retries < maxRetries) {
      const transaction = await sequelize.transaction();
      
      try {
        const account = await Account.findByPk(accountId, { transaction });
        const originalVersion = account.version;

        // Update with version check
        const [affectedRows] = await Account.update(
          { 
            ...updates, 
            version: originalVersion + 1,
            updated_at: new Date()
          },
          {
            where: { 
              id: accountId, 
              version: originalVersion 
            },
            transaction
          }
        );

        if (affectedRows === 0) {
          throw new Error('OPTIMISTIC_LOCK_ERROR');
        }

        await transaction.commit();
        return { status: 'SUCCESS', version: originalVersion + 1 };

      } catch (error) {
        await transaction.rollback();
        
        if (error.message === 'OPTIMISTIC_LOCK_ERROR' && retries < maxRetries - 1) {
          retries++;
          // Wait before retry with exponential backoff
          await new Promise(resolve => setTimeout(resolve, Math.pow(2, retries) * 100));
          continue;
        }
        
        throw error;
      }
    }
  }

  // Pessimistic locking for critical updates
  async freezeAccount(accountId, reason) {
    const transaction = await sequelize.transaction();

    try {
      // Exclusive lock to prevent any other operations
      const account = await Account.findByPk(accountId, {
        lock: Transaction.LOCK.UPDATE,
        transaction
      });

      if (!account) {
        throw new Error('Account not found');
      }

      if (account.status === 'FROZEN') {
        throw new Error('Account already frozen');
      }

      await account.update({
        status: 'FROZEN',
        freeze_reason: reason,
        frozen_at: new Date()
      }, { transaction });

      // Log the freeze action
      await TransactionModel.create({
        account_id: accountId,
        type: 'ACCOUNT_FREEZE',
        amount: 0,
        description: `Account frozen: ${reason}`,
        processed_by: 'ADMIN'
      }, { transaction });

      await transaction.commit();
      return { status: 'SUCCESS', message: 'Account frozen successfully' };

    } catch (error) {
      await transaction.rollback();
      throw error;
    }
  }
}

// Usage examples
const financialService = new FinancialService();

// Example 1: Money transfer
async function handleTransfer() {
  try {
    const result = await financialService.transferMoney(101, 102, 1000.00);
    console.log('Transfer successful:', result);
  } catch (error) {
    console.error('Transfer failed:', error.message);
  }
}

// Example 2: Batch salary processing
async function processSalaries() {
  try {
    const employeeIds = [1, 2, 3, 4, 5];
    const result = await financialService.processSalaryBatch(employeeIds);
    console.log('Salary batch processed:', result);
  } catch (error) {
    console.error('Salary processing failed:', error.message);
  }
}

module.exports = FinancialService;