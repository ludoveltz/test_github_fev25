# Initial sandwich orders
sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", 
                  "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", 
                  "Pastrami sandwich"]

print("Initial orders:", sandwich_orders)

# Remove all Pastrami sandwiches
print("\n❌ Removing Pastrami sandwiches (out of stock)...")
while "Pastrami sandwich" in sandwich_orders:
    sandwich_orders.remove("Pastrami sandwich")

print("Orders after Pastrami removal:", sandwich_orders)

# Create empty list for finished sandwiches
finished_sandwiches = []

# Process orders
print("\n👨‍🍳 Preparing sandwiches:")
while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)
    print(f"Making {current_sandwich}...")
    finished_sandwiches.append(current_sandwich)

# Print completion messages
print("\n✅ Completed orders:")
for sandwich in finished_sandwiches:
    print(f"I made your {sandwich.lower()}")