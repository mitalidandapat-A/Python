# Write a program in Python to find the sum of digits of a number
def sum_of_digits(number):
    # Convert the number to a string to iterate over each digit
    digits = str(number)
    
    # Sum up the integer value of each digit
    total = sum(int(digit) for digit in digits)
    
    return total

# Get user input
user_input = int(input("Enter a number: "))

# Calculate the sum of digits
result = sum_of_digits(user_input)

# Print the result
print(f"The sum of the digits is: {result}")
