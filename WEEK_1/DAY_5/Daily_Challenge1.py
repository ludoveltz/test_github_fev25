def sort_words():
    # Get input from user
    try:
        user_input = input("Enter words separated by commas: ")
        
        # List comprehension to split and sort words
        sorted_words = ','.join(sorted([word.strip() for word in user_input.split(',')]))
        
        # Print result
        print(f"\nSorted words: {sorted_words}")
        
    except Exception as e:
        print(f"An error occurred: {e}")

# Test the program
if __name__ == "__main__":
    sort_words()