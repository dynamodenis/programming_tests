def strStr(self, haystack: str, needle: str) -> int:
        result = -1
        for i in range((len(haystack) + 1) - len(needle)):
            if haystack[i: i + len(needle)]  == needle:
                print(f"found {haystack[i: i + len(needle)]} at {i}")
                return i
        return result
    
"""Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

 

Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.

Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
"""