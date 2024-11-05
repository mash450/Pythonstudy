# Write a program that prints the largest of 4 inputs taken in from a user. Assume that the user would not enter any two numbers which are the same.


num1=int(input("enter number 1: "))
num2=int(input ("enter number 2: "))
num3=int(input("enter number 3:"))

if num1>=num2 and num1>=num3:
    largest=num1
elif num2>=num3 and num2>=num1:
     largest=num2
else:
    num3>=num1 and num3>=num2
    largest=num3
print(f"The largest number is : {largest} ") 
