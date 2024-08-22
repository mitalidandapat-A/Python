# Print the series upto N terms: 1,2,6,24,120,720 …
import math

def print_factorial_series(n_terms):
    print("Factorial series:")
    for i in range(1, n_terms + 1):
        # Calculate the factorial of i
        factorial = math.factorial(i)
        # Print the factorial
        print(factorial, end=' ')
    print()  # For a newline after the series

# Get user input
n_terms = int(input("Enter the number of terms to display: "))

# Print the factorial series
print_factorial_series(n_terms)
