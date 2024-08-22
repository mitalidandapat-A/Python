# 5. Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops)
def reverse_list(input_list):
    # Create an empty list to store the reversed elements
    reversed_list = []
    
    # Iterate over the input list from end to start
    for i in range(len(input_list) - 1, -1, -1):
        reversed_list.append(input_list[i])
    
    return reversed_list

# Get user input
sample_list = input("Enter a list of items separated by commas: ")


# Reverse the list
reversed_sample_list = reverse_list(sample_list)

# Print the reversed list
print(f"The reversed list is: {reversed_sample_list}")
