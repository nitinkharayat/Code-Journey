"""
1Nested loops are loops within loops. The inner loop will be executed one time for each iteration of the outer loop.
Example:
"""

#################################exammmple 1 : pattern printing using nested loop###########################################
"""
1
12
123
1234
12345
12345n
pattern using nested loop"""
User_input = int(input("enter the no. to print pattern"))
c= 1
for i in range (1,User_input+1): 
    for j in range(c):
        print(j,end="")
    c = c+1
    print("")
    

