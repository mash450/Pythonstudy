fruits=['banana','apple','pineapple','grape']
for fruit in fruits:
    if fruit=='banana':
        print(fruit)
# range function

# iterate numbers from 20-100
# for num in range(20,101):
#     print(num)
# iterate numbers from 20-100 and display only even numbers
numbers=list(range(20,101))
even_numbers=[]
for i in numbers:
    if i%2==0:
     even_numbers.append(i)
print(even_numbers)

# break => used to stop the loop