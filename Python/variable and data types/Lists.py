"""
n Python, lists are ordered, mutable collections that can store mixed data types. You can create, access, modify, and remove elements, as well as iterate over them or use advanced features like nested lists and list comprehensions.

Create a list using square brackets [] or the list() constructor with an iterable.

Create a list with repeated elements using the multiplication operator *.

Access elements by index, starting at 0 for the first item or using negative indices for reverse access.

Slice lists using [start:end] to get a sublist without modifying the original.

Add elements with append() for single items, extend() for multiple items, or insert() for a specific position.

Clear all elements from a list using clear()"""

#Example of lists 
#Example 1: creating a even odd list 
Even_list = [0,2,4,6,8,10]
Odd_lisnt = [1,3,5,7,9,11]

"list are mutable , and have anny datatype"
example_list = [12,"123",123.12,True]
print(f"Not changed list {example_list}")
example_list[2] = 1 
print(f"Changed list {example_list}")