"""
In Python, there are several standard (built-in) data types that are used to store different kinds of values.

They are generally grouped into categories:

1. Text Type
str → String (sequence of Unicode characters)
Example: "Hello", 'Python'
2. Numeric Types
int → Integer numbers (no decimal)
Example: 10, -5
float → Floating-point numbers (decimal)
Example: 3.14, -0.5
complex → Complex numbers
Example: 2 + 3j
3. Sequence Types
list → Ordered, mutable collection
Example: [1, 2, 3]
tuple → Ordered, immutable collection
Example: (1, 2, 3)
range → Sequence of numbers
Example: range(5)
4. Mapping Type
dict → Key-value pairs
Example: {"name": "John", "age": 25}
5. Set Types
set → Unordered, unique elements
Example: {1, 2, 3}
frozenset → Immutable set
Example: frozenset({1, 2, 3})
6. Boolean Type
bool → Logical values True or False
7. Binary Types
bytes → Immutable sequence of bytes
bytearray → Mutable sequence of bytes
memoryview → Memory view object
✅ Total main built-in standard data types: 14
(str, int, float, complex, list, tuple, range, dict, set, frozenset, bool, bytes, bytearray, memoryview)

"""
#we can find the type of data using the type() function in python
#for example:
first_variable = "This is my first variable" # it is a string variable
print(type(first_variable)) # it will print <class 'str'> beacause type is string 
second_variable = 10 # it is an integer variable
print(type(second_variable)) # it will print <class 'int'> beacause type is integer

