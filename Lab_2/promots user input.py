# Write a program in Python that prompts the user to input a number and prints its multiplication table
def print_multiplication_table(number):
    print(f"Multiplication table for {number}:")
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")

# Get user input
user_input = int(input("Enter a number: "))

# Print the multiplication table
print_multiplication_table(user_input)
