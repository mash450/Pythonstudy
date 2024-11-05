# Write a program that takes the date of birth of a person and the
#  program outputs the age in terms of years,months,days TODAY.


# Define today's date
today_year = 2024
today_month = 11
today_day = 4

# Get the user's date of birth
dob_input = input("Enter your date of birth (YYYY-MM-DD): ")
dob_year, dob_month, dob_day = map(int, dob_input.split('-'))

# Calculate the year difference
years = today_year - dob_year

# Adjust the year if the birthday hasn't happened yet this year
if (today_month, today_day) < (dob_month, dob_day):
    years -= 1

# Calculate the month difference
months = today_month - dob_month
if today_day < dob_day:
    months -= 1  # Borrow a month if the day hasn’t been reached yet in the current month

# Adjust if months went negative
if months < 0:
    months += 12

# Calculate the day difference
# Define the number of days in each month (not considering leap years for simplicity)
days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# If today’s day is greater than or equal to the birth day, simple subtraction works
if today_day >= dob_day:
    days = today_day - dob_day
else:
    # If today’s day is less than birth day, borrow days from the previous month
    prev_month = today_month - 1 if today_month > 1 else 12
    days = (today_day + days_in_month[prev_month - 1]) - dob_day

# Output the result
print(f"Age: {years} years, {months} months, and {days} days")

