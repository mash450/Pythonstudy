 # num1= 200
# num2=500
# # sum divide,multiply,sub  etc
# x=10**5
# print(x)

# y=99//2
# print(y)

# y=99%2
# print(y)

# z=49.1234
# print(round(z,2))

# num="1000"
# num=int(num)
# num5="2000"
# num5=int(num5)
# sum=num+num5
# print(sum)

number = 56.8926
result = round(number)
print(result)  # Output: 57


number = 56.8926
result = round(number, 2)
print(result)  # Output: 56.89


number = 56.8926
result = round(number, 3)
print(result)  # Output: 56.893


temp = 56.8926

# Convert float to string
temp_str = str(temp)

# Slice and concatenate (taking everything after the decimal)
new_temp_str = temp_str[3:7]  # this takes '.8926' (ignores the 56)

# Convert back to float
new_temp = float(new_temp_str)

print(new_temp)  # Output will be 8.926
