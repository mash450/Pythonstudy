# Write a program that takes input of someone's basic salary and benefits, adds them to 
# find the gross salary then uses  the gross salary to find the NHIF. 
# To find the Kenya NHIF Rate using 


basic_salary=int(input("enter basic salary: "))
benefits=int(input("enter benefits: "))
income= basic_salary+benefits

print(f"gross income is : {income}")
if income<=5999: 
        NHIF=150
elif income<=7999:
        NHIF=300
elif income<=11999:
        NHIF=400
elif income<=14999:
        NHIF=500
elif income<=19999:
        NHIF=600
elif income<=24999:
        NHIF=750
elif income<=29999:
        NHIF=850
elif income<=34999:
        NHIF=900
elif income<=39999:
        NHIF=950
elif income<=44999:
        NHIF=1000
elif income<=49999:
        NHIF=1100
elif income<59999:
        NHIF=1200
elif income<=69999:
        NHIF=1300
elif income<=79999:
        NHIF=1400
elif income<89999:
        NHIF=1500
elif income<9999:
        NHIF=1600
else:
    NHIF=1700
print(f"NHIF contribution is: {NHIF}")


if income>=18000:
        NSSF=(income*0.06)
        print(f"NSSF is : {NSSF}")
NHDF=(income*0.015)
print(f"NHDF IS : {NHDF}")

        
    
        
    

