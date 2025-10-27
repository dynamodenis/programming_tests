    def letterCombinations(self, digits: str) -> List[str]:
        results = []
        keys = {
            '1': [],
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
            '0': [' ']
        }

        if len(digits) == 1:
            return keys[digits]
        
        # Use this backtracking
        # def backtracking(i, currStr):
        #     if len(currStr) == len(digits):
        #         results.append(currStr)
        #         return
            
        #     values = keys[digits[i]]
            
        #     for v in values:
        #         backtracking(i + 1, currStr + v)
                
        # backtracking(0, "")
        
        # You can also use this
        sol = []
        def backtracking(i):
            if i == len(digits):
                results.append("".join(sol))
                return
            
            values = keys[digits[i]]
            
            for v in values:
                sol.append(v)
                backtracking(i + 1)
                sol.pop()
                
        backtracking(0)
            
        return results
    
    
    """ 
        Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.
        Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Example 2:

Input: digits = "2"
Output: ["a","b","c"]

    """
