def is_palindrome(number):
    original_number = number
    reversed_number = 0

    while number > 0:
        remainder = number % 10
        reversed_number = (reversed_number * 10) + remainder
        number = number // 10

    return original_number == reversed_number

# Example usage:
num = int(input("Enter a number: "))
if is_palindrome(num):
    print("The number is a palindrome!")
else:
    print("The number is not a palindrome.")