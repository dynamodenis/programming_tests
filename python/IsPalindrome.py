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