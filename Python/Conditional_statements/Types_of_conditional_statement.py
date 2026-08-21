"""
There are three types of conditional statements in Python:
1. If statement: 
    The if statement is used to test a specific condition. If the condition evaluates to True, the block of code inside the if statement is executed.
2. If-else statement:
    The if-else statement is used to test a specific condition. If the condition evaluates to
    True, the block of code inside the if statement is executed. If the condition evaluates to False, the block of code inside the else statement is executed.
3. If-elif-else statement:
    The if-elif-else statement is used to test multiple conditions. If the first condition evaluates to True, the block of code inside the if statement is executed. If the first condition evaluates to False, the next condition is tested, and so on. If none of the conditions evaluate to True, the block of code inside the else statement is executed.

"""

##################Example of if,else and if-elif-else statements in Python##################

user_input = int(input("Enter a number: "))
if user_input > 0:
    print("The number is positive.")
elif user_input < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

if user_input % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

