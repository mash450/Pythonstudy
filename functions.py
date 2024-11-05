# def triangle_area():
#     base=9
#     height=4
#     area=(base*height)/2
#     return area
# p=triangle_area()
# print(p)

# def rectangle_area():
#     length=5
#     width=9
#     area=length*width
#     return area
# l=rectangle_area()
# print(l)


def area_triangle(base,height):
    area=(base*height)/2
    return area
x=area_triangle(8,9)
print(x)
y=area_triangle(4,2)
print(y)


def check_even_odd():
    # Prompt the user to enter a number
    number = int(input("Enter a number: "))
    
    # Check if the number is even or odd
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Call the function and store the result in a variable
result = check_even_odd()

# Print the result
print(f"The number is {result}.")


# function that checks the largest number

def find_largest_of_four():
    # Prompt user to enter four unique numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    num3 = float(input("Enter the third number: "))
    num4 = float(input("Enter the fourth number: "))

    # Assume the first number is the largest initially
    largest = num1

    # Compare each number with the current largest and update if needed
    if num2 > largest:
        largest = num2
    if num3 > largest:
        largest = num3
    if num4 > largest:
        largest = num4

    # Return the largest number
    return largest

# Call the function and store the result
largest_number = find_largest_of_four()

# Print the result
print(f"The largest number is: {largest_number}")

