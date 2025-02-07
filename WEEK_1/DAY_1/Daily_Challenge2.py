# Get user input
user_word = input("Enter a word: ")

# Duplicate each letter
result = ""
for letter in user_word:
    result += letter * 2 

# Display results
print(f"\nOriginal word: {user_word}")
print(f"Word with duplicates: {result}")