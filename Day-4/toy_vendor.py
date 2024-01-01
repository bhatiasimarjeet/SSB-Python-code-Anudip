print("Product code for following toys----")
print("1 for Battery Based Toys")
print("2 for Key Based Toys")
print("3 for Charging Based Toys")

toycode = int(input("Enter the toycode:"))
order_amount = float(input("Enter the order amount:"))

if(toycode == 1 and order_amount > 1000):
    order_amount -= 0.1 * order_amount
    print(f"Net pay after discount: {order_amount}")
if(toycode == 2 and order_amount > 100):
    order_amount -= 0.05 * order_amount
    print(f"Net pay after discount: {order_amount}")
if(toycode == 3 and order_amount > 500):
    order_amount -= 0.1 * order_amount
    print(f"Net pay after discount: {order_amount}")

                 