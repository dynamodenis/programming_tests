def is_palindrome_string_method(number: int):
    if number < 0:
        return False
    
    s = str(number)

    return s == s[::-1]

    
# is_palindrome_string_method(123)

def is_palindrome_math_method(number: int):
    if number < 0:
        return False
    
    if 0 <= number <= 9:
        return True
    
    original_number = number
    reversed_number = 0
    
    while number > 0:
        digit = number % 10 # Get last digit
        reversed_number = reversed_number * 10 + digit # Append the digit to the reversed number
        print(f"NUmber start {number} with digit {digit}")
        number //= 10 #Remove last digit from number. THIS IS EQUAL TO number = number // 10
        # what //= does is it takes 121 // 10 result is 12.1 then rounds off to nearest whole number (floor) so its becomes 12
        print(f"Number after {number } with digit {digit}")

    print(f"is digit {digit} reversed number {reversed_number}")

    return original_number == reversed_number
        
is_palindrome_math_method(121)

# --------------------------------------------------------LONGEST PALINDROM SUBSTRING---------------------------------
    def longestPalindrome(self, s: str) -> str:
        res = ""
        resLen = 0

        for i in range(len(s)):
           # Odd length like babad
            l,r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
            # length of the substring
                if (r-l + 1) > resLen:
                    res = s[l:r+1]
                    resLen = r-l + 1
                l -= 1
                r += 1

            # even length like cbbd
            l,r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
            # length of the substring
                if (r-l + 1) > resLen:
                    res = s[l:r+1]
                    resLen = r-l + 1
                l -= 1
                r += 1

        return res

print(f"s = 'babad' -> Longest palindromic substring: '{longestPalindrome('babad')}'")
# Expected: "bab" or "aba"

print(f"s = 'cbbd' -> Longest palindromic substring: '{longestPalindrome('cbbd')}'")
# Expected: "bb"

print(f"s = 'a' -> Longest palindromic substring: '{longestPalindrome('a')}'")
# Expected: "a"