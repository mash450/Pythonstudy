# Questions
# Convert a float to an integer with an inbuilt function in Python
# temp = 56.8926 to 57
# Convert the float below to give the results as follows
# temp = 56.8926 to 56.89 
# Convert the float below to give the results as follows
# temp = 56.8926 to 56.893 
# Convert the float below to give the results as follows
# temp=56.8926 to 8.926 
# NB: Use string  slice & concatenation, but have result as float 




# 1
number = 56.8926
result = round(number)
print(result)  # Output: 57

# 2
number = 56.8926
result = round(number, 2)
print(result)  # Output: 56.89

# 3
number = 56.8926
result = round(number, 3)
print(result)  # Output: 56.893

# 4
temp = 56.8926

# Convert float to string
temp = str(temp)

# Slice and concatenate (taking everything after the decimal)
temp = temp[3:]  # this takes '.8926' (ignores the 56)
print(temp)

temp=temp[0]+"."+temp[1:]
print(temp)

# Convert back to float
temp = float(temp)

print(temp)  # Output will be 8.926
