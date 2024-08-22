# Print a number as a 8 segment display N Lines:
def print_digit_as_7_segment_display(digit, n):
    # Define the 7-segment display patterns for digits 0-9
    segments = {
        '0': [" _ ",
              "| |",
              "|_|"],
        '1': ["   ",
              "  |",
              "  |"],
        '2': [" _ ",
              " _|",
              "|_ "],
        '3': [" _ ",
              " _|",
              " _|"],
        '4': ["   ",
              "|_|",
              "  |"],
        '5': [" _ ",
              "|_ ",
              " _|"],
        '6': [" _ ",
              "|_ ",
              "|_|"],
        '7': [" _ ",
              "  |",
              "  |"],
        '8': [" _ ",
              "|_|",
              "|_|"],
        '9': [" _ ",
              "|_|",
              " _|"]
    }

    if digit not in segments:
        raise ValueError("Digit not supported")

    pattern = segments[digit]

    # Adjust the display based on N lines
    if n == 2:
        # For N=2, only show the top and bottom segments
        print(pattern[0])
        print(pattern[2])
    elif n == 3:
        # For N=3, show all three segments
        print(pattern[0])
        print(pattern[1])
        print(pattern[2])
    elif n == 4:
        # For N=4, add an additional empty line
        print(pattern[0])
        print(pattern[1])
        print()
        print(pattern[2])
    else:
        raise ValueError("N should be 2, 3, or 4")

# Get user input
digit = input("Enter a digit (0-9): ")
n = int(input("Enter the number of lines (N, should be 2, 3, or 4): "))

# Print the 7-segment display
print_digit_as_7_segment_display(digit, n)
