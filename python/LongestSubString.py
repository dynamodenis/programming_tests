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


def longestCommonSubstringMatrix(s1: str, s2: str) -> str:
    """
    Finds the longest common substring between two given strings.

    Args:
        s1: The first input string.
        s2: The second input string.

    Returns:
        The longest common substring. If multiple substrings have the same
        maximum length, any one of them can be returned.
        Returns an empty string if no common substring exists.
    """
    len1 = len(s1)
    len2 = len(s2)

    # dp[i][j] will store the length of the longest common suffix
    # of s1[0...i-1] and s2[0...j-1]
    # Initialize a 2D array (matrix) with zeros.
    # Dimensions: (len1 + 1) x (len2 + 1) to handle empty prefixes.
    dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]

    # Variables to track the maximum length found and the ending index
    # in s1 (or s2, it doesn't matter as they are equal lengths).
    max_length = 0
    ending_index_s1 = 0

    # Fill the dp table
    # i iterates through s1's characters (1-indexed for dp table)
    for i in range(1, len1 + 1):
        # j iterates through s2's characters (1-indexed for dp table)
        for j in range(1, len2 + 1):
            # If the current characters match, increment the length from the diagonal
            if s1[i-1] == s2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
                # Update max_length and its ending_index if a new longest is found
                if dp[i][j] > max_length:
                    max_length = dp[i][j]
                    ending_index_s1 = i
            else:
                # If characters don't match, the common substring ends here, so reset to 0
                dp[i][j] = 0

    # Extract the longest common substring using max_length and ending_index_s1
    if max_length == 0:
        return "" # No common substring found

    # The substring starts at ending_index_s1 - max_length
    # and ends at ending_index_s1 (exclusive in Python slicing)
    return s1[ending_index_s1 - max_length : ending_index_s1]

# --- Test Cases ---
print(f"s1='abcde', s2='ace' -> '{longestCommonSubstring('abcde', 'ace')}'")
print(f"s1='abcde', s2='abfce' -> '{longestCommonSubstring('abcde', 'abfce')}'")