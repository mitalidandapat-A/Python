# Convert Decimal number to Binary
# Get user input
decimal_number = int(input("Enter a decimal number: "))

# Convert to binary
binary_number = bin(decimal_number)

# Print the binary representation (excluding the '0b' prefix)
print(f"Binary representation: {binary_number[2:]}")

