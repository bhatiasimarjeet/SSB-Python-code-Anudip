x = 5
print(x)

x = 10
y= 5
result = x + y
print(result)

name = input("Enter your name: ")
print(name)

x = 20 
if(x > 10):
    print("x is greater than 10")
else:
    print("x is not greater than 10")
    
    
count = 0
while (count < 9):
    print(count)
    count = count + 1
    
for i in range(5):
    print(i)
    

def add_numbers(a, b):
    return a + b
result = add_numbers(3, 7)

my_list = [1, 2, 3, 4, 5] # Create a list
my_list.append(6) # Add an element


try:
    result = 10 / 0 # Attempt to divide by zero
except ZeroDivisionError as e:
    print("Error:", e)
    
    
for i in range(10):
    if i == 5:
        break # Exit the loop when i equals 5
    if i == 3:
        continue # Skip the rest of the loop body for i equals 3
    print(i)

def square(x):
    return x ** 2 # Return the square of x
print(square(3))
    

# This is a single-line comment
result = 42 # This comment explains the purpose of the following line of code

'''
This is a multi-line comment or docstring.
It can span multiple lines and is typically used for documentation.
'''
