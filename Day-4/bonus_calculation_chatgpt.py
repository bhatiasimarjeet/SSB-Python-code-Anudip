# Ask user for input
salary = float(input("Enter your salary: "))
years_of_service = int(input("Enter your years of service: "))

# Check if years of service are more than 5 years
if years_of_service > 5:
    bonus = 0.05 * salary  # Calculate 5% of the salary as bonus
    print(f"Congratulations! Your bonus amount is ${bonus:.2f}")
else:
    print("Sorry, you are not eligible for a bonus.")