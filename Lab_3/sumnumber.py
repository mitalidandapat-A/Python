# 6. Compute the sum up to n terms in the series 1 - 1/2 + 1/3 - 1/4 + 1/5 -... 1/n where n is a positive integer and input by user
def compute_series_sum(n):
    # Initialize the sum to 0
    series_sum = 0
    
    # Compute the sum of the series
    for i in range(1, n + 1):
        if i % 2 == 0:
            # Subtract terms where the index is even
            series_sum -= 1 / i
        else:
            # Add terms where the index is odd
            series_sum += 1 / i
    
    return series_sum

# Get user input
n = int(input("Enter the number of terms (n): "))

# Compute and print the sum of the series
if n > 0:
    result = compute_series_sum(n)
    print(f"The sum of the series up to {n} terms is: {result}")
else:
    print("Please enter a positive integer.")
