# Tuples are immutable (cannot be modified)

# Create initial tuple
numbers = (1, 2, 3)
print(f"Initial tuple: {numbers}")
print(f"Type: {type(numbers)}")

# New tuple with additional elements
new_tuple1 = numbers + (4, 5)
print(f"1. new tuple: {new_tuple1}")