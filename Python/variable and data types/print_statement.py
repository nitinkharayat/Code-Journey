first_variable = "This is my first variable" # it is a string variable
second_variable = 10 # it is an integer variable
third_variable = 10.5 # it is a float variable
"""
In python we can print the variable values and their data types using the print() function
or many ther ways to print the variable values and their data types but the most common way is to use the print() function
for exmple

"""
print("first_variable:", first_variable, "type:", type(first_variable))#this will print the value of first_variable and its data type
print(f"second_variable: {second_variable}, type: {type(second_variable)}")#this is f-string method to print the variable value and its data type
print(f"""
hi {first_variable}
    hello {second_variable}""")#this is multi-line f-string method to print the variable value and its data type


print("hello "+ first_variable  )#this is concatenation method to print the variable value and its data type

print(first_variable,end=" ")#this will print the value of first_variable and its data type in the same line and end as line with space
print(second_variable,end=" ")