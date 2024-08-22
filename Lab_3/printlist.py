#  Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
def print_list(lst):
    # Print each element of the list
    for item in lst:
        print(item)

# Get user input
input_list = input("Enter a list of items separated by commas: ")


input_list = [item.strip() for item in input_list.split(',')]

# Print the list
print_list(input_list)
