# Accept a sentence as input
input_sentence = input("Enter a sentence: ")

# Initialize counters for letters and digits
letters_count = 0
digits_count = 0

# Iterate through each character in the sentence
for char in input_sentence:
    if char.isalpha():
        letters_count += 1
    elif char.isdigit():
        digits_count += 1

# Print the counts
print(f"LETTERS {letters_count}")
print(f"DIGITS {digits_count}")
