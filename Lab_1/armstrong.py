def is_perfect_number(number):
    if number < 1:
        return False
    
    # Find the sum of the proper divisors
    sum_of_divisors = sum(i for i in range(1, number) if number % i == 0)
    
    # Check if the sum of the proper divisors equals the number
    return sum_of_divisors == number

# Example usage
number = 28
if is_perfect_number(number):
    print(f"{number} is a perfect number.")
else:
    print(f"{number} is not a perfect number.")
