"""
->variable name should be start with a letter or underscore
->variable name can only contain letters, numbers, and underscores
->variable name should not be a reserved word or keyword
->variable name should be descriptive and meaningful(not nessecary but good for readability , preferably use camelCase or snake_case)
->it is a case sensitive language, so variable names with different cases are treated as different variables
"""
first_variable = "This is my first variable" # it is a string variable

second_variable = 10 # it is an integer variable

third_variable = 10.5 # it is a float variable

fourth_variable = True # it is a boolean variable

fifth_variable = [1, 2, 3, 4, 5] # it is a list variable

sixth_variable = (1, 2, 3, 4, 5) # it is a tuple variable

seventh_variable = {1, 2, 3, 4, 5} # it is a set variable

eighth_variable = {"name": "John", "age": 30, "city": "New York"} # it is a dictionary variable

ninth_variable = None # it is a NoneType variable

tenth_variable = b"Hello World" # it is a bytes variable

eleventh_variable = bytearray(b"Hello World") # it is a bytearray variable

twelfth_variable = memoryview(b"Hello World") # it is a memoryview variable

thirteenth_variable = complex(1, 2) # it is a complex variable

fourteenth_variable = range(10) # it is a range variable

"""the data types of the above variables are as follows:
Python variables can hold different data types:

Numeric Types: int, float, complex
Sequence Types: list, tuple, range
Text Type: str
Mapping Type: dict
Set Types: set, frozenset
Boolean Type: bool
Binary Types: bytes, bytearray, memoryview
None Type: NoneType
and there are many more data types available in Python, but these are the most commonly used ones.
"""
#we can print the variable values and their data types using the print() function 

print("first_variable:", first_variable)


