# Ask user for input
quantity = int(input("Enter the quantity you want to purchase: "))
cost_per_unit = 100  # Cost per unit is $100

# Calculate total cost
total_cost = quantity * cost_per_unit

# Apply discount if total cost is more than 1000
if total_cost > 1000:
    discount = 0.1 * total_cost  # Calculate 10% discount
    total_cost -= discount  # Subtract discount from total cost

print(f"The total cost for {quantity} units is ${total_cost:.2f}")