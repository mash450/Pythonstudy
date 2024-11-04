# Write a program which accepts email as form input or from terminal. Validate the email by checking if it's a valid email. 
# Hint: Check if it contains an “@” symbol and “.” symbol.

# Number of emails to validate
num_emails = int(input("Enter the number of emails to validate: "))

# Loop to accept and validate each email
for i in range(num_emails):
    # Accept email input from the user
    email = input(f"Enter email {i + 1}: ")

    # Validate the email
    if "@" in email and "." in email:
        print(f"Email {i + 1}: Valid")
    else:
        print(f"Email {i + 1}: Invalid")
