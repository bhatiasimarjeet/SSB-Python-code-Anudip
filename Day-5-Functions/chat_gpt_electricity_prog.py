def calculate_bill(installed_load, energy_consumed):
    # Define the tariff slabs
    slab_1_rate = 4.75
    slab_2_rate = 5.75
    slab_3_rate = 7
    slab_4_rate = 8

    # Calculate the bill based on tariff slabs
    if energy_consumed <= 50:
        total_cost = energy_consumed * slab_1_rate
    elif energy_consumed <= 100:
        total_cost = 50 * slab_1_rate + (energy_consumed - 50) * slab_2_rate
    elif energy_consumed <= 200:
        total_cost = 50 * slab_1_rate + 50 * slab_2_rate + (energy_consumed - 100) * slab_3_rate
    else:
        total_cost = 50 * slab_1_rate + 50 * slab_2_rate + 100 * slab_3_rate + (energy_consumed - 200) * slab_4_rate
    
    # Adding additional charges based on installed load
    fixed_charges = installed_load * 50  # Assuming Rs. 50 per kW
    total_cost += fixed_charges
    
    return total_cost

# Example usage:
installed_load = 5  # Example installed load in kW
energy_consumed = 150  # Example energy consumed in kWh

total_bill = calculate_bill(installed_load, energy_consumed)
print(f"The total electricity bill is Rs. {total_bill:.2f}")