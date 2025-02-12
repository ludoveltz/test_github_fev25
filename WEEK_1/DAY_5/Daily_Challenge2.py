def longest_word(sentence):
    try:
        # Split the sentence into words
        words = sentence.split()
        
        # Find the longest word using max() with len as key
        longest = max(words, key=len)
        
        return longest
        
    except Exception as e:
        return f"An error occurred: {e}"

# Test function with examples
def test_longest_word():
    # Test cases
    test_cases = [
        "Margaret's toy is a pretty doll.",
        "A thing of beauty is a joy forever.",
        "Forgetfulness is by all means powerless!"
    ]
    
    # Run tests
    for test in test_cases:
        result = longest_word(test)
        print(f"\nSentence: {test}")
        print(f"Longest word: {result}")

# Run the tests
if __name__ == "__main__":
    test_longest_word()