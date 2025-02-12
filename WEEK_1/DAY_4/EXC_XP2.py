def average_length_of_words(sentence):
    # Split the sentence into words
    words = sentence.split()
    
    # Calculate the total length of all words
    total_length = sum(len(word) for word in words)
    
    # Calculate the average length of words
    average_length = total_length / len(words)
    
    # Round the result to one decimal place
    return round(average_length, 1)

# Example usage
result = average_length_of_words('only four lett erwo rdss')
print(result)  # Output: 4.0