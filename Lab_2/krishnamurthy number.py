9. 
# 10. Write a program in Python to check if a number is Krishnamurthy number
import math

def is_krishnamurthy_number(n):
    # Convert the number to a string to iterate over its digits
    digits = str(n)
    
    # Calculate the sum of the factorials of the digits
    sum_of_factorials = sum(math.factorial(int(digit)) for digit in digits)
    
    # Check if the sum of factorials equals the original number
    return sum_of_factorials == n

# Get user input
number = int(input("Enter a number: "))

# Check if the number is a Krishnamurthy number
if is_krishnamurthy_number(number):
    print(f"{number} is a Krishnamurthy number.")
else:
    print(f"{number} is not a Krishnamurthy number.")
