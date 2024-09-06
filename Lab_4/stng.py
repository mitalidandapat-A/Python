def check_string(input_string):
    if input_string in ["yes", "YES", "Yes"]:
        print("Yes")
    else:
        print("No")

# Example usage
input_string = input("Enter a string: ")
check_string(input_string)