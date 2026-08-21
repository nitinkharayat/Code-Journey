"""
Parameter : a variable inside the function,runs when no input is given to function but the function is called
Argument : actual value inside the function 

"""

"""
For the showcase of that work jus see the comments 
"""
#Example 1:A function which is used when call to find the odd and even  number 
def OddEven(hello):#Here hello is parameter 
    Number = int(input("Enter the number =>"))
    hello = Number
    if Number % 2 == 0 :
        print(f"The given number {input} is even number ")
    else:
        print(f"The given number  {input} is odd number")

#Example 2: A function which is used to print the table 

def Multiplication():#No parameter in this function 
    Number = int(input("Enter the number =>"))
    count = 1
    for i in range(Number+1):
        print(f"{Number} X {count} = {Number*count}")

#Calling the above function in main brach if user wants 
while True:
    print("\n0.Press 0 and enter key for exiting the program. \n\n1.Press 1 and enter key  if you want to find the odd and even number. \n\n2.Press 2 if you want to print the table. \n")
    User_input = int(input("Press the button to continue ==>"))
    if User_input==0:
        break
    elif User_input == 1:
        OddEven()#if the value in is bracket tthen the value is arguement
    elif User_input==2:
        Multiplication()#if the value in is bracket tthen the value is arguement
    else:
        invalid= input("Invalid button pressed \n Press Enter to continue")
