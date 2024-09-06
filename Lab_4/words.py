# Accept a sequence of whitespace-separated words as input
input_sequence = input("Enter a sequence of whitespace-separated words: ")

# Split the input string into a list of words
words_list = input_sequence.split()

# Remove duplicate words by converting the list to a set
unique_words = set(words_list)

# Sort the unique words alphanumerically
sorted_unique_words = sorted(unique_words)

# Join the sorted list back into a whitespace-separated sequence
output_sequence = ' '.join(sorted_unique_words)

# Print the output sequence
print(output_sequence)
