def longestSubstring(s: str):
    if not s:
        return 0
    
    left = 0
    charSet = set()
    maximum = 0
    
    for right in (range(len(s))):
        char = s[right]
        while char in charSet:
            charSet.remove(s[left])
            left += 1
        charSet.add(char)
        
        maximum = max(maximum, right-left + 1) # SInce python strings start at 0, we add 1 to corrrectly get the lenght of substring
        
    return maximum
    
    
longestSubstring("abcabcbb")