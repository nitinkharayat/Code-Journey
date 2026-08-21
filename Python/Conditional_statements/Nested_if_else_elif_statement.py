"""
The nested if-else statement is a conditional statement that allows you to test multiple conditions within another if or else statement.
It is used when you want to check for additional conditions after the initial condition has been evaluated.
It is if inside another if or else statement. The nested if-else statement can be used to create more complex decision-making structures in your code.
"""


###################Example of nested if-else statement in Python##################

User_input = int(input("Enter a positive number to check whether it is even or odd: "))
if User_input > 0:
    print("The number is positive.")
    if User_input % 2 == 0:
        print("The number is even.")
    else:
        print("The number is odd.")
else:
    print("The number is not positive.")