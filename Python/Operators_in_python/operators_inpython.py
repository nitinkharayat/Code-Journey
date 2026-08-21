"""
Arithmetic operators are used to perform mathematical operations between numeric values. The following are the arithmetic operators available in Python:
1. Addition (+): Adds two numbers together.
2. Subtraction (-): Subtracts one number from another.
3. Multiplication (*): Multiplies two numbers together.
4. Division (/): Divides one number by another and returns a float.
5. Floor Division (//): Divides one number by another and returns the largest integer less than or equal to the result.
6. Modulus (%): Returns the remainder of a division operation.
7. Exponentiation (**): Raises one number to the power of another.
The precedence table of operators is as follows:
1. Parentheses ()
2. Exponentiation (**)
3. Multiplication (*) and Division (/) and Floor Division (//) and Modulus (%)
4. Addition (+) and Subtraction (-)
5. Comparison operators (==, !=, >, <, >=, <=)
6. Logical operators (and, or, not)
7. Assignment operators (=, +=, -=, *=, /=, //=, %=, **=)

"""


First_input = int(input("Enter first number: ")) # this will take input from the user and store it in the variable first_input in the form of integer
Second_input = int(input("Enter second number: ")) # this will take input from the user
print(f"Addition of {First_input} and {Second_input} is: {First_input + Second_input}") # this will print the addition of first_input and second_input
print(f"Subtraction of {First_input} and {Second_input} is: {First_input - Second_input}") # this will print the subtraction of first_input and second_input
print(f"Multiplication of {First_input} and {Second_input} is: {First_input * Second_input}") # this will print the multiplication of first_input and second_input
print(f"Division of {First_input} and {Second_input} is: {First_input / Second_input}") # this will print the division of first_input and second_input
print(f"Floor Division of {First_input} and {Second_input} is: {First_input // Second_input}") # this will print the floor division of first_input and second_input         
print(f"Square root of {First_input} is: {First_input ** 0.5}") # this will print the square root of first_input
print(f"Square root of {Second_input} is: {Second_input ** 0.5}\n\n\n") # this will print the square root of second_input


#Above are arthmetic operators in python and their precedence table.

"""
Now the comparison operators are used to compare two values and return a boolean value (True or False) based on the comparison. The following are the comparison operators available in Python:
it has only boolean values as output.
1. Equal to (==): Returns True if the values on both sides are equal, otherwise returns False.
2. Not equal to (!=): Returns True if the values on both sides are not equal, otherwise returns False.
3. Greater than (>): Returns True if the value on the left is greater than the value on the right, otherwise returns False.
4. Less than (<): Returns True if the value on the left is less than the value on the right, otherwise returns False.
5. Greater than or equal to (>=): Returns True if the value on the left is greater than or equal to the value on the right, otherwise returns False.
6. Less than or equal to (<=): Returns True if the value on the left is
    less than or equal to the value on the right, otherwise returns False.
"""

#Example of comparison operators in python
First_comparison_input = int(input(" To check the comparison operator: \n Enter first number:  ")) # this will take input from the user and store it in the variable first_input in the form of integer
Second_comparison_input = int(input("Enter second number: ")) # this will take input from the user and store it in the variable second_input in the form of integer
print(f"Is {First_comparison_input} equal to {Second_comparison_input}? {First_comparison_input == Second_comparison_input}") # this will print the result of the comparison of first_input and second_input
print(f"Is {First_comparison_input} not equal to {Second_comparison_input}? {First_comparison_input != Second_comparison_input}") # this will print the result of the comparison of first_input and second_input
print(f"Is {First_comparison_input} greater than {Second_comparison_input}? {First_comparison_input > Second_comparison_input}") # this will print the result of the comparison of first_input and second_input
print(f"Is {First_comparison_input} less than {Second_comparison_input}? {First_comparison_input < Second_comparison_input}") # this will print the result of the comparison of first_input and second_input
print(f"Is {First_comparison_input} greater than or equal to {Second_comparison_input}? {First_comparison_input >= Second_comparison_input}\n\n\n\n") # this will print the result of the comparison of first_input and second_input


"""
The logical operators are used to combine multiple boolean expressions and return a boolean value based on the logical relationship between them. The following are the logical operators available in Python:
1. and: Returns True if both expressions are True, otherwise returns False.
2. or: Returns True if at least one of the expressions is True, otherwise returns False
3. not: Returns True if the expression is False, and returns False if the expression is True.
"""

#Example of logical operators in python
First_logical_input = int(input(" To check the logical operator: \n Enter first number: ")) # this will take input from the user and store it in the variable first_logical_input in the form of integer
Second_logical_input = int(input("Enter second number: ")) # this will take input from the user and store it in the variable second_logical_input in the form of integer
print(f"Is {First_logical_input} and {Second_logical_input} both True? {First_logical_input and Second_logical_input}") # this will print the result of the logical AND operation
print(f"Is {First_logical_input} or {Second_logical_input} True? {First_logical_input or Second_logical_input}") # this will print the result of the logical OR operation
print(f"Is {First_logical_input} False? {not First_logical_input}") # this will print the result of the logical NOT operation