# Function to reverse a string
def reverse_string(input_string):
    return input_string[::-1]

# Function to check if a string is a palindrome
def is_palindrome(input_string):
    reversed_string = reverse_string(input_string)
    return input_string == reversed_string

# Function to check if a string ends with a specific substring
def ends_with(input_string, substring):
    return input_string.endswith(substring)

# Function to capitalize the first letter of each word in a string
def capitalize_first_letter(input_string):
    return input_string.title()

# Function to check if two strings are anagrams
def are_anagrams(string1, string2):
    return sorted(string1) == sorted(string2)

# Function to remove vowels from a string
def remove_vowels(input_string):
    vowels = 'aeiouAEIOU'
    return ''.join([char for char in input_string if char not in vowels])

# Function to find the length of the longest word in a sentence
def length_of_longest_word(sentence):
    words = sentence.split()
    longest_word = max(words, key=len)
    return len(longest_word)

# Main function to demonstrate the above functionalities
def main():
    input_string = input("Please enter a string: ")
    substring = input("Please enter a substring to check if the string ends with it: ")
    
    # Demonstrating each functionality
    reversed_string = reverse_string(input_string)
    print(f"Reversed string: {reversed_string}")
    
    is_palindrome_result = is_palindrome(input_string)
    print(f"Is the string a palindrome? {'Yes' if is_palindrome_result else 'No'}")
    
    ends_with_result = ends_with(input_string, substring)
    print(f"Does the string end with '{substring}'? {'Yes' if ends_with_result else 'No'}")
    
    capitalized_string = capitalize_first_letter(input_string)
    print(f"String with capitalized first letters: {capitalized_string}")
    
    # For anagram check, taking another input string
    another_string = input("Please enter another string to check for anagram: ")
    are_anagrams_result = are_anagrams(input_string, another_string)
    print(f"Are the strings anagrams? {'Yes' if are_anagrams_result else 'No'}")
    
    string_without_vowels = remove_vowels(input_string)
    print(f"String without vowels: {string_without_vowels}")
    
    # For finding the longest word length, assuming input_string is a sentence
    longest_word_length = length_of_longest_word(input_string)
    print(f"Length of the longest word in the sentence: {longest_word_length}")

# Run the main function
if __name__ == "__main__":
    main()
