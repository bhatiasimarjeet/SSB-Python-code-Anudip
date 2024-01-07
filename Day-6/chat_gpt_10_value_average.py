total = 0
count = 0

while count < 10:
    try:
        num = int(input("Enter an integer: "))
        total += num
        count += 1
    except ValueError:
        print("Please enter a valid integer.")

if count > 0:
    average = total / count
    print(f"The average of the {count} integers is: {average}")
else:
    print("No valid integers were entered.")