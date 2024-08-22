def check_season(month):
    # Define seasons based on the month
    if month in ['December', 'January', 'February']:
        return 'Winter'
    elif month in ['March', 'April', 'May']:
        return 'Spring'
    elif month in ['June', 'July', 'August']:
        return 'Summer'
    elif month in ['September', 'October', 'November']:
        return 'Autumn'
    else:
        return 'Invalid month'

# Get user input
user_month = input("Enter the month: ").capitalize()

# Determine and print the season
season = check_season(user_month)
print(f"The season in {user_month} is {season}.")

