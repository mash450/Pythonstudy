# Prompt the user for a number either on a form input or the terminal. Depending on whether the number is even or odd, display  either “odd” or “even” to the user.
#  Hint: how does an even / odd number react differently when divided by 2?
# Once you learn functions,revisit this and write this code inside a function.
# Extras:
# If the number is a multiple of 4, print out “divisible by 4

number=int(input("enter a number: "))
if number%2==0:
    if number%4==0:
        print("number is even and divisible by 4")
    else:
        print("number is only even")
else:
    if number%4==0:
        print("number is only divisible by 4")
    else:
        print("number is neither even nor divisible by 4")