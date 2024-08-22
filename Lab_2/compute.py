# Compute a)5 to the power of 8 b)square root of 400 c)exponent of 5 d)Logarithm of 625 base 5
import math

# Function to compute and print the results
def compute_math_operations():
    # a) 5 to the power of 8
    power_result = 5 ** 8
    print(f"5 to the power of 8 is: {power_result}")

    # b) Square root of 400
    sqrt_result = math.sqrt(400)
    print(f"The square root of 400 is: {sqrt_result}")

    # c) Exponent of 5 (e^5)
    exp_result = math.exp(5)
    print(f"The exponent of 5 (e^5) is: {exp_result}")

    # d) Logarithm of 625 base 5
    log_result = math.log(625, 5)
    print(f"The logarithm of 625 base 5 is: {log_result}")

# Call the function to compute and display the results
compute_math_operations()
