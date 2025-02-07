
# Get user input
number = int(input("Enter a number: "))
length = int(input("Enter the length of the list: "))

# Create list of multiples
multiples = []
for i in range(1, length + 1):
    multiples.append(number * i)

# Display result
print(f"\nMultiples of {number} with length {length}:")
print(multiples)