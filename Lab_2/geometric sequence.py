# 13. Write a Python program to print the first 6 terms of a geometric sequence starting with 2 and having a common ratio of 3
def print_geometric_sequence(first_term, common_ratio, num_terms):
    print(f"Geometric sequence with first term {first_term} and common ratio {common_ratio}:")
    term = first_term
    for i in range(num_terms):
        print(term, end=' ')
        term *= common_ratio
    print()  # For a newline after the sequence

# Get user inputs
first_term = float(input("Enter the first term of the geometric sequence: "))
common_ratio = float(input("Enter the common ratio of the geometric sequence: "))
num_terms = int(input("Enter the number of terms to display: "))

# Print the geometric sequence
print_geometric_sequence(first_term, common_ratio, num_terms)
