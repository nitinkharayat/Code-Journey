"""
A return statement ends function execution and optionally passes a value back to the caller.

In Python, the return statement is used inside a function to end its execution and send a value back to the caller.
If no value is specified, Python automatically returns None.
A return statement can return any Python object — numbers, strings, lists, dictionaries, functions, classes, or even multiple values packed in a tuple.
"""

###########example of return function 
def Addition(first,second):
    c = first+second 
    return c 
def NoneValuefunction(first,second):
    c = first+second
a = int(input("enter 1 number"))
b = int(input("enter 2 number"))
answer = Addition(a,b)
print(answer)
"""If no return in function then it has saved Nonevalue"""
print(NoneValuefunction(12,12))