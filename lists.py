fruits= ['mango',[1,2,3,4,5], 'banana', 100, 30.5, False,True]
print(type(fruits))
# accessing elements inside a list
print(fruits[1])
print(fruits[1][4])
# modify elements
fruits[0]='water melon'
print(fruits)

# append method =>used to add elements in a list
fruits.append("oranges")
print(fruits)

# insert=>used to insert elements at a specific index
fruits.insert(1,1000)
print(fruits)
# insert apple at index 5
fruits.insert(5,'apple')
print(fruits)

# remove function
num=[10,20,30,40,50,10]
num.remove(10)
print(num)
# remove 50
num=[10,20,30,40,50,10,50]
num.remove(50)
print(num)

# pop =>remove items of a specific index
num.pop(0)
print(num)

# slicing list
print(num[0:3])

# len=>for displaying lenghth of variable
print(len(num))

# check if element is in list
name=["Kenya","Uganda","Tanzania","Ethiopia"]
print("Kenya"in name)


list1=[1,2,3,4,5,6]
list2=[7,8,9,0]
list3=list1+list2
print(list3)
