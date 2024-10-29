#    Take three inputs from a user, separately. Print the largest of the numbers.
#     Hint: Determine what type of data is taken in as input

num1=float(input("enter the first number:"))
num2=float(input("enter the second number:"))
num3=float(input("enter the third number:"))
if num1>num2 and num1>num3:
    largest=num1
elif num2>num1 and num2>num3:
    largest=num2
else:
    largest=num3
    print(f"{largest} is the largest")




#  Take as input from a user the temperature if the temperature is above 30°C display “The temperature is too 
# high”,if the temperature is above 15 display “Normal temperature” otherwise display “Cold temperature

temp=30
if temp>30:
    print("the temperature is too high")
elif temp>15:
    print("normal temperature")
else:
    print("cold temperature")



#  Write a Python program that checks if a variable x is between 10 and 20 (inclusive)
#  and if another variable y is greater than 100. If both conditions are true, print "Conditions met", otherwise print 
# "Conditions not met"

x=float(input("enter a number x:"))
y=float(input("enter a number y:"))
if 10<=x<=20 and y>100:
    print("conditions met")
else:
    print("conditions not met")


# 4. Write a Python program that checks if a variable password is equal to the string "secret123". If it is, print "Access   
# granted", otherwise print "Access denied

password=input('enter password:')
correct_password="secret123"
if password==correct_password:
    print("access granted")
else:
    print("access denied")

# 5. Write a Python program that checks if a variable student_score is greater than 90. If true, check if the attendance is 
# greater than 80. If both conditions are true, print "Excellent student", otherwise print "Good score, but attendance 
# needs improvement"

student_score=float(input("enter score:"))
attendance=float(input("enter attendance"))
if student_score>90:

    if attendance>80:
        print("excellent student")

    else:
        print("good score but attendance needs improvement")
else:
  print("score needs improvement")


