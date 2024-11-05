# Write a program that takes the email and password as 
# input from a user and checks if they are equal to “admin@mail.com” and password is “Admin@123” , if so then print  “Login is Successful” and if not print “Invalid username or password”. ONLY accept 3 tries after which it notifies you that you have been blocked.


correct_email="admin@email.com"
correct_password="Admin@123"
attempts=3

for i in range(attempts):
    password=input("enter password: ")
    email=input("enter email address: ")
    if password==correct_password and email==correct_email:
        display="access granted"
        break
    else:
        remaining_attempts=attempts-(i+1)
        print(f"incorrect password or email ypu have {remaining_attempts} attempts remaining")
else:
    attempts==3
    print("your account is blocked")
print(display)