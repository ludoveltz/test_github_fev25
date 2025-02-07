# Create a set with favorite numbers
my_fav_numbers = {7, 13, 22, 42, 99}
print("My favorite numbers:", my_fav_numbers)

# Add two new numbers to the set
my_fav_numbers.add(8)
my_fav_numbers.add(15)
print("After adding numbers:", my_fav_numbers)

# Remove the last number
my_fav_numbers.remove(15)
print("After removing a number:", my_fav_numbers)

# Create friend's favorite numbers set
friend_fav_numbers = {3, 10, 27, 42, 88}
print("Friend's favorite numbers:", friend_fav_numbers)

# Concatenate both sets
our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
print("Our favorite numbers:", our_fav_numbers)