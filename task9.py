# Write a program called stars. It should prompt the user for a number, and it should print the number of stars till the number entered.
# Example If rows is 5, it should print the following:
# *
# **
# ***
# ****
# *****.....


# Prompt the user for a number of rows
rows = int(input("Enter the number of rows: "))

# Loop through each row
for i in range(1, rows + 1):
    # Print stars equal to the current row number
    print('*' * i)
