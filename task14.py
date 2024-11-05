# Write a program that takes input of 2 values 
# and adds them. The program should only accept numbers and floats only or otherwise display 
# an error “invalid character entered” and take the user to re-enter the inputs .


while True:
    num1=input("enter first number: ")  
    if (num1.replace('.','',1).isdigit()) or (num1[0]=='-'and num1[1:].replace('.','',1).isdigit()):
        num1=float(num1)
    else:
        print("invalid character entered")
        continue
    num2=input("enter the second number")
    if (num2.replace('.','',1).isdigit()) or (num2[0]=='-'and num2[1:].replace('.','',1).isdigit()):
        num2=float(num2)
    else:
        print("invalid character entered")
    break
result=num1+num2
print(result)