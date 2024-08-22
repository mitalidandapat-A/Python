# Write a function to calculate the power of a number using recursion
def power(base, exponent):
    if exponent == 0:
        return 1
    else:
        return base * power(base, exponent - 1)

# Get user input
base = float(input("Enter the base number: "))
exponent = int(input("Enter the exponent: "))

# Call the function and print the result
result = power(base, exponent)
print(f"{base} raised to the power of {exponent} is {result}")
