import random

# Generate 5 random numbers
random_numbers = [random.randint(1, 100) for _ in range(5)]

# Display the generated numbers
print("Generated numbers:", random_numbers)

# Calculate and display the maximum and minimum numbers
maximum_number = max(random_numbers)
minimum_number = min(random_numbers)

print(f"Maximum number: {maximum_number}")
print(f"Minimum number: {minimum_number}")