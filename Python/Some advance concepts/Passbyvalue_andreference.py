import copy
L1 = []
def pass_by_reference(ref_value):
    ref_value = copy.copy(ref_value)
    ref_value[0]=1
    print(ref_value)
    L1.append(id(ref_value)==id(Ref_value))
Ref_value = [13,14,15]
pass_by_reference(Ref_value)
print(Ref_value,L1)