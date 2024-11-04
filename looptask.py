# Write a program that displays a numbers 1 to 50 inside a list.
# From 1 above display the ones divisible by 7 or 5 inside a list.
# Find sum and average of values in the range between 10 to 40.
# Put in a list the first 10 odd numbers between 10 to 50. 
# write a program that takes a number as input and prints its multiplication table up to 10 using a for loop.
# write a program that counts and prints the number of even numbers between 1 and 50 using a for loop
# ls1 = [ (“Jay”, 20), (“Mo”, 30), (“Mya”, 32) ]
# Display the total quantity of the 3 above.

numbers=list(range(1,51))
num=[ ]
for i in numbers:
    num.append(i)
print(num)


# question2
numbers=list(range(1,51))
num=[ ]
for i in numbers:
     if i%7==0 or i%5==0:
      num.append(i)
print(num)

# question3
    # Find sum and average of values in the range between 10 to 40.
values=list(range(10,41))
sum=sum(values)
average=sum/len(values)
print("sum of values is: ", sum)
print("average of values is: " ,average)


# question 4
# Put in a list the first 10 odd numbers between 10 to 50. 

values=list(range(10,51))
oddnum=[]
for i in values:
   if i%2!=0:
      oddnum.append(i)
      if len(oddnum)==10:
         break
print(oddnum)


# question 5
# write a program that takes a number as input and prints its multiplication table up to 10 using a for loop.
# Take a number as input from the user
number = int(input("Enter a number: "))

# Print the multiplication table up to 10
print(f"Multiplication Table for {number}:")
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")

# question 6
# write a program that counts and prints the number of even numbers between 1 and 50 using a for loop
numbers=list(range(1,50))
even_numbers=[]
for i in numbers:
   if i%2==0:
      even_numbers.append(i)
print("even numbers is :" ,even_numbers)
print("length of even numbers is :" ,len(even_numbers))


# question 7
# ls1 = [ (“Jay”, 20), (“Mo”, 30), (“Mya”, 32) ]
# Display the total quantity of the 3 above.
# Define the list
ls1 = [("Jay", 20), ("Mo", 30), ("Mya", 32)]

# Initialize a variable to store the total quantity
total_quantity = 0

# Loop through each tuple in the list and add the quantity to the total
for name, quantity in ls1:
    total_quantity += quantity

# Display the total
print("Total quantity:", total_quantity)

