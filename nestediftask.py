# Write a program that:
# Takes a transaction amount and account type ("Standard" or "Premium") as input.
# If the account type is "Standard":
# Check if the amount is above 500:
# If it is, print "Transaction exceeds the limit for Standard accounts."
# If not, print "Transaction approved."
# If the account type is "Premium":
# Check if the amount is above 1,000:
# If it is, print "Transaction exceeds the limit for Premium accounts."
# If not, print "Transaction approved.

transaction_amount = float(input("Enter the transaction amount: "))
account_type = input("Enter the account type (Standard or Premium): ").lower().strip()


if account_type == "Standard":
        if transaction_amount > 500:
            print("Transaction exceeds the limit for Standard accounts.")
        else:
            print("Transaction approved.")
elif account_type == "Premium":
        if transaction_amount > 1000:
            print("Transaction exceeds the limit for Premium accounts.")
        else:
            print("Transaction approved.")
else:
        print("Invalid account type.")


