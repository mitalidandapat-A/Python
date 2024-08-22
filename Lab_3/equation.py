# Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculatesolution set of a quadratic equation, solve_quadratic_eqn
import math  # Import cmath to handle complex roots

def solve_quadratic(a, b, c):
    # Calculate the discriminant
    discriminant = b**2 - 4*a*c
    
    # Calculate two solutions using the quadratic formula
    root1 = (-b + math.sqrt(discriminant)) / (2*a)
    root2 = (-b - math.sqrt(discriminant)) / (2*a)
    
    return root1, root2

# Get user input
a = float(input("Enter the coefficient a: "))
b = float(input("Enter the coefficient b: "))
c = float(input("Enter the coefficient c: "))

# Ensure 'a' is not zero to prevent division by zero
if a == 0:
    print("Coefficient 'a' cannot be zero in a quadratic equation.")
else:
    # Calculate and print the roots
    root1, root2 = solve_quadratic(a, b, c)
    print(f"The roots of the quadratic equation are: {root1} and {root2}")
