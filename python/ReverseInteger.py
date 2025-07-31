class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1 #Check if number is negative -321 or positive 321
        x = abs(x) #take absoulte number without any sign
        rev = str(x)[::-1] #reverse using slicing
        rev_int = int(rev) * sign # Multiple by sign to add initial sign like x * -1 = -X

        if rev_int < -2**31 or rev_int > 2**31 - 1: #Check if value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
            return 0

        return rev_int


# Input: x = 123
# Output: 321

# Input: x = -123
# Output: -321