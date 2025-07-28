function generateParenthesis(n) {
    // Only return if the total number of n is 2 times n
    // Only add OPen if open is less than n
    // Only add Close if close is less than open
    const result = [];
    
    function backtrack(current, open, close) {
        if (current.length === 2 * n) {
            result.push(current);
            return;
        }
        
        if (open < n) {
            backtrack(current + '(', open + 1, close);
        }
        
        if (close < open) {
            backtrack(current + ')', open, close + 1);
        }
    }
    
    backtrack('', 0, 0);
    return result;
}

// Example usage:
const n = 3;
const parenthesesCombinations = generateParenthesis(n);
console.log(parenthesesCombinations);
// Output: ["((()))","(()())","(())()","()(())","()()