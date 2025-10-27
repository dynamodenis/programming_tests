def longestCommonPrefix(strs: List[str]) -> str:
    result = ""
    for i in range(len(strs[0])):
        for s in strs:
            if i == len(s) or s[i] != strs[0][i]:
                return result
            
        # Only add the character if all strings have the same character at position i, so all have to go through the string loop firtst before adding
        result += strs[0][i]

    return result

"""Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

 """