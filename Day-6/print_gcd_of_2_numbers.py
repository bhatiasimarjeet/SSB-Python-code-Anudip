# Input two numbers from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
# Find the minimum of the two numbers
min_num = min(num1, num2)
# Initialize variables to store the GCD/HCF and the current divisor
gcd = 1
divisor = 1
# Use a while loop to find the GCD/HCF
while divisor <= min_num:
    if num1 % divisor == 0 and num2 % divisor == 0:
        gcd = divisor
    divisor += 1
# Display the GCD/HCF
print(f"The GCD/HCF of {num1} and {num2} is {gcd}")