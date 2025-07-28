def longestValidParentheses(s: str) -> int:
    """
    Given a string containing just the characters '(' and ')',
    return the length of the longest valid (well-formed) parentheses substring.

    Args:
        s: The input string consisting only of '(' and ')'.

    Returns:
        The length of the longest valid parentheses substring.
    """
    max_length = 0
    # Initialize a stack with -1. This acts as a base for calculating lengths
    # and handles cases where the first valid substring starts at index 0.
    stack = [-1]

    for i in range(len(s)):
        char = s[i]

        if char == '(':
            # If an opening parenthesis, push its index onto the stack.
            stack.append(i)
        else: # char == ')'
            # If a closing parenthesis, pop the top element from the stack.
            stack.pop()

            # If the stack becomes empty after popping, it means the current
            # closing parenthesis doesn't have a matching opening parenthesis
            # within the current valid sequence. Push the current index
            # as a new base for future calculations.
            if not stack:
                stack.append(i)
            # If the stack is not empty, it means we found a valid pair.
            # The length of this valid substring is the current index 'i'
            # minus the index of the new top of the stack (which is the
            # index of the last unmatched opening parenthesis or the base -1).
            else:
                max_length = max(max_length, i - stack[-1])
    
    return max_length

# --- Test Cases ---
print(f"s = '(()' -> Longest valid parentheses: {longestValidParentheses('(()')}")
# Expected: 2 (for "()")

print(f"s = ')()())' -> Longest valid parentheses: {longestValidParentheses(')()())')}")
# Expected: 4 (for "()()")

print(f"s = '' -> Longest valid parentheses: {longestValidParentheses('')}")
# Expected: 0

print(f"s = '()(()' -> Longest valid parentheses: {longestValidParentheses('()(()')}")
# Expected: 2 (for "()")

print(f"s = '()(())' -> Longest valid parentheses: {longestValidParentheses('()(())')}")
# Expected: 6 (for "()(())")

print(f"s = '((()))' -> Longest valid parentheses: {longestValidParentheses('((()))')}")
# Expected: 6 (for "((()))")

print(f"s = '()(()())' -> Longest valid parentheses: {longestValidParentheses('()(()())')}")
# Expected: 8 (for "()(()())")
