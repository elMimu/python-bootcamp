from math import pow 

a, v = input().split()

a = float(a)
v = float(v)

pot = pow(a, v)

print("{:.4f}".format(pot))



