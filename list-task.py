#  trainees = ["John", [2, ["James","Mary"]]]
#  1. Display 2 from the list.
#  2. Output James  from the list.
#  3. Using a method add 56 at the end of the list.
#  4. Using a method add the name Mike between James and Mary
#  5. Change the value of 2 to 8
#  6. Remove John and Mary from the list.
#  7. Using a function, determine the length of the list
#  Initial list
trainees = ["John", [2, ["James", "Mary"]]]
print(trainees[1][0])  # Output: 2

# 2
print(trainees[1][1][0])

# 3


trainees.append(56)
print(trainees)  # Output: ['John', [2, ['James', 'Mary']], 56]

# 4
trainees[1][1].insert(1, "mike")
print(trainees)

# 5
trainees[1][0]= 8
print(trainees)


# 6

['John', [8, ['James', 'mike', 'Mary']], 56]
# Remove John
trainees.remove("John")

# Remove Mary (found inside the nested list)
trainees[0][1].remove("Mary")

print(trainees)

# 7
trainees=len(trainees)
print(trainees)



