# Set the correct password and maximum attempts
correct_password = "admin@123"
max_attempts = 4

# Loop through attempts
# for attempt in range(1, max_attempts + 1):
#     # Ask for user input
#     password = input(f"Attempt {attempt} - Enter your password: ")
    
#     # Check if the entered password matches the correct password
#     if password == correct_password:
#         print("Access granted.")
#         break
#     else:
#         print("Incorrect password.")
        
#     # Check if all attempts have been used
#     if attempt == max_attempts:
#         print("Account is blocked.")


attempts=4
correct_password="admin@123"
for i in range(attempts):
    password=input("enter password: ")
    if password==correct_password:
        display="access granted"
        break
    else:
        remaining_attempts= attempts-(i+1)
        print (f"incorrect password you have {\
             remaining_attempts} attempts remaining" )
        if remaining_attempts==0:
            print("account blocked")
     
print(display)





