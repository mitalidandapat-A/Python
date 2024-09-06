def process_string(input_string):
    # Calculate the length of the string
    length_of_string = len(input_string)
    print(f"Length of the string: {length_of_string}")

    # Find the substring "country"
    if "country" in input_string:
        print("The substring 'country' is present in the string.")
    else:
        print("The substring 'country' is not present in the string.")

    # Count the occurrences of each word in the given sentence
    words = input_string.split()
    word_count = {}
    for word in words:
        word = word.strip('.,')  # Remove punctuation
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    print("Word occurrences:")
    for word, count in word_count.items():
        print(f"{word}: {count}")

# Input string
input_string = "India is my motherland. I love my country. Capital of India is New Delhi"

# Call the function
process_string(input_string)
