# When you are given al problem to find all basic solutions or bruteforce use Backtracking

def generateParenthesis_using_stack(n: int):
    # only add open paranthesis if open < n
    # only add closing parenthesis if closed < open
    # valid if open == closed == n
    stack = []
    results = []
    def recursive_backtracking(open, close):

        if open == close == n:
            results.append("".join(stack))
            return
        if open < n:
            stack.append("(")
            recursive_backtracking(open+1, close)
            stack.pop() # After all open combination remove the stack elements for backtracking
            
        if close < open:
            stack.append(")")
            recursive_backtracking(open, close + 1)
            stack.pop() # After all close combination remove the stack elements for backtracking
            
    recursive_backtracking(0, 0)
    return results
            
# generateParenthesis_using_stack(3)
            

def generateParenthesis_using_string(n: int):
    # only add open paranthesis if open < n
    # only add closing parenthesis if closed < open
    # valid if open == closed == n
    
    results = []
    def recursive_backtracking(current_string: str, open:int, close:int):
        print(f" Open {open} Close {close} with stack {current_string}")

        if open == close == n:
            results.append(current_string)
            print(f"we have a finished result {results}")
            return
        if open < n:
            recursive_backtracking(current_string + "(", open+1, close)
            
        if close < open:
            recursive_backtracking(current_string + ")", open, close + 1)
            
    recursive_backtracking("",0, 0)
    
    print(f"results {results}")
    return results
            
generateParenthesis_using_string(3)
# Output ['((()))', '(()())', '(())()', '()(())', '()()()']       