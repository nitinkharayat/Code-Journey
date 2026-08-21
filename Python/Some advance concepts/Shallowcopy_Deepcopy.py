import copy
a = [12,13,13,21]
b = a#only copying the id 
print(id(a)==id(b))
##here comes the otput true
"""shallow copy
"""
Sh1 = [12,13,45,[13,14],13]
Sh2 = Sh1.copy
sh3 = copy.copy(Sh1)
print(id(Sh1)==(Sh2))
print(id(Sh1)==(sh3))
"""
Deep copy
"""
Dc1 = [12,14,15,[12,13,14,],12]
Dc2 = copy.deepcopy(Dc1)
print(id(Dc1)==id(Dc2))