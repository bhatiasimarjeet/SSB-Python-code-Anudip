import math

side_1 = float(input("Enter the dimension of side 1 of triangle: "))

side_2 = float(input("Enter the dimension of side 2 of triangle: "))

side_3 = float(input("Enter the dimension of side 3 of triangle: "))

semi_perimeter = (side_1 + side_2 + side_3) / 2

area_of_triangle = math.sqrt(semi_perimeter * (semi_perimeter - side_1) * (semi_perimeter - side_2) * (semi_perimeter - side_3))

print(area_of_triangle)

