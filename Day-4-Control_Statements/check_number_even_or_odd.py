# Accept a number from the user
user_input = input("Enter a number: ")
# Convert the user input to an integer
number = int(user_input)
# Check if the number is even
if number % 2 == 0:
    print(f"{number} is an even number.")