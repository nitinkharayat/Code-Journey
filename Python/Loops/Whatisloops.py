"""
Loops are the set of code that are executed repeatedly until a certain condition is met. 
In Python, there are two methods of loops: for loops and while loops.

loops are  of many type for example : nested loops, infinite loops, etc. In this script, we will demonstrate the use of for loops and while loops in Python.
"""

"""
1. For Loops:
For loops are used to iterate over a sequence (like a list, tuple, dictionary, set
, or string) and execute a block of code for each item in the sequence.
Example:
"""
For_input = int(input("Enter a number for for loop: "))
# Using a for loop to print numbers from 0 to the user input
print("For loop starts : \n")
for i in range(For_input):
    print(i,end=", ")

"""
2. While Loops:
While loops are used to execute a block of code as long as a specified condition is true.
Example:
"""
While_input = int(input("Enter a number: for while loop: "))
# Using a while loop to print numbers from 0 to the user input
i = 0
print("While loop starts : \n")
while i < While_input:
    print(i,end=", ")
    i += 1
