class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result, sub = [], []

        def backtrack(i):
            if i >= len(s):
                result.append(sub.copy())
                return

            # Loop through remaining letters
            for j in range(i, len(s)):
                # check is the letter is a palindrome
                if self.isPalindrome(s, i, j):
                    sub.append(s[i:j+1])
                    backtrack(j+1)
                    sub.pop()

        backtrack(0)
        print(result)
        return result

    def isPalindrome(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False

            l, r = l+1, r -1

        return True
    
"""
Given a string s, partition s such that every of the partition is a

. Return all possible palindrome partitioning of s.

 

Example 1:

Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]

Example 2:

Input: s = "a"
Output: [["a"]]

 
"""