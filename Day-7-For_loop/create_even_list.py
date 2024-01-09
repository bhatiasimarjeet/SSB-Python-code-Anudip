numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = [] #here we are using an empty list.
for number in numbers:
    if number % 2 == 0:
        evens.append(number)
print(evens)