# Dictionary mapping month numbers to seasons
seasons = {
    1: 'Winter', 2: 'Winter', 3: 'Spring',
    4: 'Spring', 5: 'Spring', 6: 'Summer',
    7: 'Summer', 8: 'Summer', 9: 'Autumn',
    10: 'Autumn', 11: 'Autumn', 12: 'Winter'
}

# Get the month number from the user
month_number = int(input("Enter the month number (1-12): "))

# Check if the month number is valid
if 1 <= month_number <= 12:
    # Print the corresponding season
    print(f"The season for month {month_number} is {seasons[month_number]}.")
else:
    print("Invalid month number! Please enter a number between 1 and 12.")
