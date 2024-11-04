# Write a program which gets a phone number from a form input or terminal. Validates the phone number by checking if it starts with +254.. or 07.. or 7… or 254.. or 01... or  1.. Convert the number to start with +254… 
# e.g if a user enters “0712345678”, the program should display “+254712345678”
# e.g if a user enters “0112345678”, the program should display “+254112345678”
# e.g if a user enters “712345678”, the program should display “+254712345678”

phone_number=int(input("enter phone number :"))
phone_number=str(phone_number)
if phone_number[:4]=="+254":
    formatted_number=phone_number
elif phone_number[:2]=="07" or phone_number[:2]=="01":
    formatted_number="+254" + phone_number[1:]
elif phone_number [:1]=="7" or phone_number[:1]=="1":
    formatted_number="+254" + phone_number
elif phone_number [:3]=="254":
    formatted_number="+254" + phone_number[3:]
else:
    formatted_number="invalid number"
phone_number=int(phone_number)
print("formatted number is : ", formatted_number)