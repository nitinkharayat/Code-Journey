"""
While loop : While loops are used to execute a block of code as long as a specified condition is true.
example:
"""

###############################################Example 1 : for printing table using while loop###########################################
User_input = int(input("Enter a number for table printing: "))
# Using a while loop to print the multiplication table of the user input
print(f"Multiplication table of {User_input}:")
c = 1
while c <= 10:
    print(f"{User_input} x {c} = {User_input * c}")
    c += 1


##############################################Example 2 : for printing even number using while loop###########################################
Even_input = int(input("Enter a number for even number printing: "))
# Using a while loop to print even numbers from 0 to the user input
print(f"Even numbers from 0 to {Even_input}:")
c = 0 
while c <= Even_input:
    if c % 2 == 0:
        print(c, end=", ")
        c += 1
    else:
        c += 1
        continue

