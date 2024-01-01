distance  = int(input("Enter the distance:"))

if(distance > 1 and distance <= 50):
    charges = distance * 8
    print(f"Total Charges: {charges}")
elif(distance > 50 and distance <= 100):
    charges = distance * 10
    print(f"Total Charges: {charges}")
elif(distance > 100):
    charges = distance * 12
    print(f"Total Charges:{charges}")
else:
    print("Enter correct input")