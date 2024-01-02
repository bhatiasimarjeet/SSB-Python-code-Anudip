def square_function(number):
    result_of_square = number * number
    return result_of_square

num = int(input("Enter a number to find the square: "))
print(f"The result of square:",square_function(num))
