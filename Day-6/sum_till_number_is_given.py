
sum = 0
while(True):
    num = int(input("Enter a number(0 to quit and display the sum): "))
    sum = sum + num
    if(num == 0):
        break
print("Sum of entered numbers is: ",sum)