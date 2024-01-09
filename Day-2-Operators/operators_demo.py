a = 8
b = 7

is_equal = (a == b)
is_not_equal = (a != b)
is_less_than = (a < b)
print(is_equal)
print(is_not_equal)
print(is_less_than)

x = True
y = False
result_and = x and y
result_or = x or y
result_not = not x
print(result_and)
print(result_or)
print(result_not)

x = 5
x += 2 # Equivalent to x = x + 2
print(x)

a = 5 # Binary: 0101
b = 3 # Binary: 0011
bitwise_and = a & b # Result: 0001 (Decimal: 1)
print(bitwise_and)

#declare list
fruits = ["apple", "banana", "cherry"]
#Declare string
is_apple_in_list = "apple" in fruits
is_mango_not_in_list = "mango" not in fruits
print(is_apple_in_list)
print(is_mango_not_in_list)

x = [1, 2, 3]
y = x
is_same_object = x is y
print(is_same_object)


# Specifying a dummy number
number = 17  # You can replace this with any number you want to check

# Using ternary operator to check if the number is even or odd
result = "Even" if number % 2 == 0 else "Odd"

# Printing the result
print(f"The number {number} is {result}.")

base = 3  # You can change this to any base number
exponent = 4  # You can change this to any exponent

# Calculating the power using the '**' operator
result = base ** exponent

# Printing the result
print(f"{base} raised to the power of {exponent} is: {result}")
