def remove_consecutive_duplicates():
    # Get the word from user
    word = input("Enter a word: ")
    
    # Using iteration
    def remove_duplicates_iteration(text):
        if not text:  # Check if string is empty
            return text
            
        result = text[0]  # Start with first character
        
        # Compare each character with the previous one
        for i in range(1, len(text)):
            if text[i] != text[i-1]:  # If current char is different from previous
                result += text[i]
                
        return result

# Test the program
if __name__ == "__main__":
    # Test with multiple examples
    test_cases = [
        "ppoeemm",
        "wiiiinnnnd",
        "ttiiitllleeee",
        "cccccaaarrrbbonnnnn"
    ]
        
    # Test cases
    print("\nTest Cases:")
    for test in test_cases:
        print(f"\nTesting: {test}")
        result = test[0] + ''.join(b for a, b in zip(test, test[1:]) if a != b)
        print(f"Result: {result}")