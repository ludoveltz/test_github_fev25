class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

# Instantiate three Cat objects
cat1 = Cat("Whiskers", 3)
cat2 = Cat("Paws", 5)
cat3 = Cat("Claws", 2)

# Function to find the oldest cat
def find_oldest_cat(*cats):
    oldest_cat = max(cats, key=lambda cat: cat.age)
    return oldest_cat

# Find the oldest cat
oldest_cat = find_oldest_cat(cat1, cat2, cat3)

# Print the result
print(f"The oldest cat is {oldest_cat.name}, and is {oldest_cat.age} years old.")

### Explanation:

# We create three instances of the `Cat` class, each with a name and an age.
# Function `find_oldest_cat`:** This function takes a variable number of `Cat` objects and uses the `max` function with a lambda to find the cat with the highest age.
# Printing the Result:** We use an f-string to format and print the name and age of the oldest cat.