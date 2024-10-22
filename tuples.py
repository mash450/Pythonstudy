marks= (100,300,250,160,700,800)
print(type(marks))
# converting to a list
marks=list(marks)
print(type(marks))
# converting back to a tuple
marks=tuple(marks)
print(type(marks))

days=("sunday","monday","tuesday","wednesday","thursday","friday","saturday")
# replace "thursday" with "thur"
days=list(days)
days[4]="thur"
print(days)
days=tuple(days)
print(type(days))

# display wednesday
print(days[3])

# length
days=len(days)
print(days)






