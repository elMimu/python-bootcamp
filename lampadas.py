n = int(input())
v = input().split()
A = 0
B = 0

for i in range(len(v)):
	v[i] = int(v[i])

##p

for elemento in v:
	if elemento == 1:
		A = 1 - A
	else:
		A = 1 - A
		B = 1 - B

print(A)
print(B)
