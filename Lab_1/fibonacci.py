def fibonacci_up_to_n(n):
    # List to store the Fibonacci series
    fibonacci_series = []
    
    # Initial two Fibonacci numbers
    a, b = 0, 1
    
    # Generate Fibonacci series up to n
    while a <= n:
        fibonacci_series.append(a)
        a, b = b, a + b
    
    return fibonacci_series

# Example usage
n = 100
print(f"Fibonacci series up to {n}: {fibonacci_up_to_n(n)}")
