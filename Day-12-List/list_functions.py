my_list = [1, 2, 3, 4, 5]
length = len(my_list) # length is 5

my_list = [1, 2, 3]
my_list.append(4) # Adds 4 to the end: [1, 2, 3, 4]

my_list = [1, 2, 3]
my_list.extend([4, 5]) # Extends with [4, 5]: [1, 2, 3, 4, 5]

my_list = [1, 2, 4]
my_list.insert(2, 3) # Inserts 3 at index 2: [1, 2, 3, 4]

my_list = [1, 2, 3, 2]
my_list.remove(2) # Removes the first 2: [1, 3, 2]

my_list = [1, 2, 3, 4]
popped_item = my_list.pop(2) # Removes and returns 3, list becomes [1, 2, 4]

my_list = [10, 20, 30, 20]
index = my_list.index(20) # index is 1

my_list = [1, 2, 3, 4, 5]
exists = 5 in my_list # Check if 5 is in the list
index = my_list.index(4) # Find the index of 4 (returns 3)

my_list = [1, 2, 2, 3, 2]
count = my_list.count(2) # count is 3

my_list = [3, 1, 2]
my_list.sort() # Sorts the list: [1, 2, 3]

my_list = [3, 1, 2]
sorted_list = sorted(my_list) # sorted_list is [1, 2, 3], my_list remains [3, 1, 2]

my_list = [1, 2, 3]
my_list.reverse() # Reverses the list: [3, 2, 1]

my_list = [1, 2, 3]
copied_list = my_list.copy() # Creates a copy of my_list