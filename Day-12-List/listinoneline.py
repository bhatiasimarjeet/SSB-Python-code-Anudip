fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

my_list = [1, 2, 3, 4, 5]
# Create a new list with squared elements
squared_list = [x ** 2 for x in my_list]
# Print each element multiplied by 2
print("Square of all the numbers are")
[print(x * 2) for x in my_list]

my_list = [1, 2, 3, 4, 5]
index = 0
while index < len(my_list):
    print(my_list[index])
    index += 1
