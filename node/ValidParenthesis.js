function isValidParentheses(s) {
    const stack = []; // Our stack to store opening brackets
    
    // Map to store corresponding opening brackets for each closing bracket
    const map = {
        ')': '(',
        '}': '{',
        ']': '['
    };

    for (let i = 0; i < s.length; i++) {
        const char = s[i];

        // If it's an opening bracket, push it onto the stack
        if (char === '(' || char === '{' || char === '[') {
            stack.push(char);
        } 
        // If it's a closing bracket
        else if (char === ')' || char === '}' || char === ']') {
            // If stack is empty, means a closing bracket appeared without an opener
            if (stack.length === 0) {
                return false;
            }

            const lastOpen = stack.pop(); // Get the most recent opening bracket

            // Check if the popped opening bracket matches the current closing bracket
            if (lastOpen !== map[char]) {
                return false; // Mismatch in type
            }
        }
        // If the character is not a bracket, you might want to ignore it or return false
        // For this specific problem, we assume only brackets are in the string.
    }

    // After iterating, if the stack is empty, all brackets were matched
    return stack.length === 0;
}

// Test Cases:
console.log(`"()": ${isValidParentheses("()")}`);            // true
console.log(`"()[]{}": ${isValidParentheses("()[]{}")}`);    // true
console.log(`"{[()]}" : ${isValidParentheses("{[()]}")}`);   // true
console.log(`"([)]": ${isValidParentheses("([)]")}`);        // false (incorrect order)
console.log(`"{": ${isValidParentheses("{")}`);              // false (unclosed)
console.log(`"())": ${isValidParentheses("())")}`);          // false (unopened closing)
console.log(`"": ${isValidParentheses("")}`);                // true (empty string is valid)
console.log(`"({[": ${isValidParentheses("({[")}`);          // false (unclosed)
console.log(`"]": ${isValidParentheses("]")}`);              // false (closing without opener)
console.log(`"foo(bar[baz])": ${isValidParentheses("foo(bar[baz])")}`); // false if only brackets are expected
                                                                       // true if non-brackets are ignored