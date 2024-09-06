# Function to count characters in a string
def count_characters(input_string):
    # Create an empty dictionary to store character counts
    char_count = {}
    
    # Iterate over each character in the input string
    for char in input_string:
        # If the character is already in the dictionary, increment its count
        if char in char_count:
            char_count[char] += 1
        # If the character is not in the dictionary, add it with a count of 1
        else:
            char_count[char] = 1
    
    # Return the dictionary with character counts
    return char_count

# Function to print the character counts
def print_char_counts(char_count):
    # Sort the dictionary by key (character)
    sorted_chars = sorted(char_count.items())
    
    # Print each character and its count
    for char, count in sorted_chars:
        print(f"{char},{count}")

# Main function
def main():
    # Get input string from the user
    input_string = input("Please enter a string: ")
    
    # Count the characters in the input string
    char_count = count_characters(input_string)
    
    # Print the character counts
    print_char_counts(char_count)

# Run the main function
if __name__ == "__main__":
    main()
