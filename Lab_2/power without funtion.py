# 15. Write a Python program that prompts the user to enter a base number and an exponent, and then calculates the power of the base to the exponent. The program should not use the
# exponentiation operator (**) or the math.pow() function
def calculate_power(base, exponent):
    result = 1
    # Loop to multiply the base with itself exponent times
    for _ in range(exponent):
        result *= base
    return result

# Get user input
base = float(input("Enter the base number: "))
exponent = int(input("Enter the exponent: "))

# Calculate the power
power = calculate_power(base, exponent)

# Print the result
print(f"{base} raised to the power of {exponent} is {power}")
