def create_letter_index():
    # Get word from user
    word = input("Please enter a word: ").lower()
    
    # Create empty dictionary
    letter_index = {}
    
    # Loop through each character and its index
    for index, letter in enumerate(word):
        # Convert letter to string explicitly to ensure it's a string
        letter = str(letter)
        
        # If letter exists in dictionary, append index to its list
        if letter in letter_index:
            letter_index[letter].append(index)
        # If letter doesn't exist, create new list with index
        else:
            letter_index[letter] = [index]
    
    # Print result
    print(f"\nWord: '{word}'")
    print("Letter indexes:", letter_index)
    
    # Print type verification (optional, for demonstration)
    print("\nVerification of types:")
    for letter, indexes in letter_index.items():
        print(f"Letter '{letter}' is of type: {type(letter)}")
        print(f"Indexes {indexes} is of type: {type(indexes)}")

# Run the program
create_letter_index()