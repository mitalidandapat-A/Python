# 8. Write a program to compute cosine of x. The user should supply x and a positive integer n. We compute the cosine of x using the series and the computation should use all terms in the
# series up through the term involving xn cos x = 1 - x2/2! + x4/4! - x6/6! ....
import math

def compute_cosine(x, n):
    cosine_sum = 0 
    
    
    for i in range(n):
        term = ((-1)** i *(x ** (2 * i)))/ math.factorial(2 * i)
        cosine_sum += term
        
    
    return cosine_sum

# Example usage:
x = float(input("Enter the value of x (in radians): "))
n = int(input("Enter a positive integer n (number of terms): "))

result = compute_cosine(x, n)
print(f"cos({x}) using {n} terms is approximately: {result}")
