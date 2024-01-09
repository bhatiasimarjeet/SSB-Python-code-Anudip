def is_armstrong_number(number):
    num_str = str(number)
    num_digits = len(num_str)
    total = 0
    
    for digit in num_str:
        total += int(digit) ** num_digits
    
    return total == number

# Example usage:
num = int(input("Enter a number: "))
if is_armstrong_number(num):
    print("The number is an Armstrong number!")
else:
    print("The number is not an Armstrong number.")