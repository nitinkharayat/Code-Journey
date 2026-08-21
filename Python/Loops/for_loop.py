"""
For Loop : It is used to iterate over a sequence (like a list, tuple, dictionary, set, or string) and execute a block of code for each item in the sequence.
example:
for i in range(5):
    print(i)

"""


###########################################for loop example for table printing ###########################################
User_input = int(input("Enter a number for table printing: "))
# Using a for loop to print the multiplication table of the user input
print(f"Multiplication table of {User_input}:")
for i in range(1, 11):
    print(f"{User_input} x {i} = {User_input * i}")


###########################################For loop exaample 2 :For printing even number ###########################################
Even_input = int(input("Enter a number for even number printing: "))
# Using a for loop to print even numbers from 0 to the user input
print(f"Even numbers from 0 to {Even_input}:")
for i in range(Even_input + 1):
    if i % 2 == 0:
        print(i, end=", ")
    else:
        continue
    