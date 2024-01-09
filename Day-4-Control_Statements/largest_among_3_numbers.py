number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
number3 = int(input("Enter third number: "))

if(number1 > number2 and number1 > number3):
    print("Number 1 is greater than number 2 and number 3")
if(number2 > number1 and number2 > number3):
    print("Number 2 is greater than number 1 and number 3")
if(number3 > number1 and number3 > number2):
    print("Number 3 is greater than number 1 and number 2")