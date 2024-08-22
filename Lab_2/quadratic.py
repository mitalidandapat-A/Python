# To solve the quadratic equation
import math

# Get user input for the coefficients
a = float(input("Enter the coefficient a: "))
b = float(input("Enter the coefficient b: "))
c = float(input("Enter the coefficient c: "))

# Calculate the discriminant
discriminant = b**2 - 4*a*c

# Check the nature of the discriminant
if discriminant > 0:
    # Two real and distinct roots
    root1 = (-b + math.sqrt(discriminant)) / (2 * a)
    root2 = (-b - math.sqrt(discriminant)) / (2 * a)
    print(f"The equation has two real and distinct roots: {root1} and {root2}")
elif discriminant == 0:
    # One real root (both roots are the same)
    root = -b / (2 * a)
    print(f"The equation has one real root: {root}")
else:
    # Complex roots
    realPart = -b / (2 * a)
    imaginaryPart = math.sqrt(-discriminant) / (2 * a)
    print(f"The equation has two complex roots: {realPart} + {imaginaryPart}i and {realPart} - {imaginaryPart}i")
