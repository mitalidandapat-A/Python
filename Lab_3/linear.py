# Write a function called calculate_slope which return the slope of a linear equation
def calculate_slope(x1, y1, x2, y2):
    # Check if x1 and x2 are the same to avoid division by zero
    if x2 == x1:
        return 'Undefined slope (vertical line)'
    else:
        # Calculate the slope
        slope = (y2 - y1) / (x2 - x1)
        return slope

# Get user input
x1 = float(input("Enter the x-coordinate of the first point (x1): "))
y1 = float(input("Enter the y-coordinate of the first point (y1): "))
x2 = float(input("Enter the x-coordinate of the second point (x2): "))
y2 = float(input("Enter the y-coordinate of the second point (y2): "))

# Calculate and print the slope
slope = calculate_slope(x1, y1, x2, y2)
print(f"The slope of the line is: {slope}")
