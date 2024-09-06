# Accept a comma-separated sequence of words as input
input_sequence = input("Enter a comma-separated sequence of words: ")

# Split the input string into a list of words
words_list = input_sequence.split(',')

# Sort the list of words alphabetically
sorted_words_list = sorted(words_list)

# Join the sorted list back into a comma-separated sequence
output_sequence = ','.join(sorted_words_list)

# Print the output sequence
print(output_sequence)
