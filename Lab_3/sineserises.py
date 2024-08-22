# 7. Write a program to compute sin x for given x. The user should supply x and a positive integer n. We compute the sine of x using the series and the computation should use all terms in the series up through the term involving xn
# sin x = x - x3/3! + x5/5! - x7/7! + x9/9! ........
import math

def compute_sine(x, n):
    # Initialize the sine value
    sine_value = 0
    
    # Compute sine using the series expansion
    for i in range(n):
        # Calculate the term index (2i + 1) for the current term
        term = ((-1)** i *(x ** (2 * i+1)))/ math.factorial(2 * i+1)
        # Calculate the term value
        sine_value +=  term
    
    return sine_value

# Get user input
x = float(input("Enter the value of x (in radians): "))
n = int(input("Enter the number of terms (n): "))

result = compute_sine(x, n)
print(f"The sine of {x} using {n} terms is: {result}")

   
