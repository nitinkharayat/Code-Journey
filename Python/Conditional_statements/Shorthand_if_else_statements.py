"""
This is a Python script that demonstrates the use of shorthand if-else statements, also known as ternary operators.
It allows for a more concise way to write conditional statements in Python.

"""

###################Example of shorthand if-else statement in Python##################

user_input = int(input("Enter a number: "))
# Using shorthand if-else statement to check if the number is positive or negative
result = "positive" if user_input > 0 else "negative"
print(f"The number is {result}.")
#Using simple if-else statement to check if the number is even or odd
if user_input % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")