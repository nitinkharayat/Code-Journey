#python can convert variables from one data type to another data type using implicit and explicit conversion
#implicit conversion is done by python automatically when we perform operations on different data types
#explicit conversion is done by the user using built-in functions like int(), float(), str(), etc.

##################################for example of implicit conversion#####################################
x = 10 # it is an integer variable
y = 10.5 # it is a float variable   
z = x + y # python automatically converts the integer variable x to float variable and then performs the addition operation
print(z) # it will print 20.5 because python automatically converts the integer variable x
print(f"the data type of z is: {type(z)}") # it will print <class 'float'> because python automatically converts the integer variable x to float variable

################################for example of explicit conversion#####################################
a = 10 # it is an integer variable
b = 10.5 # it is a float variable
c = str(a) + str(b) # we are explicitly converting the integer variable a to string variable and then performing the concatenation operation
print("c=="+c) # it will print 1010.5 because we are explicitly converting the integer
print(f"the data type of c is: {type(c)}") # it will print <class 'str'> because we are explicitly converting the integer variable a to string variable
#for any float variable we can use the int() function to convert it to integer variable and for any integer variable we can use the float() function to convert it to float variable 
#the int will be lower than the float variable because the int() function will remove the decimal part of the float variable and return only the integer part of the float variable
####################################example of explicit conversion from float to int#####################################
d = 10.9 # it is a float variable
print(f"the data type of d =={d} is: {type(d)}") # it will print <class 'float'> because d is a float variable
e = int(d) # we are explicitly converting the float variable d to integer variable using the
print(f"the data type of e=={e} is: {type(e)}") # it will print <class 'int'> because we are explicitly converting the float variable d to integer variable
