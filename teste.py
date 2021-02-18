n = int(input())

v = input().split()

for i in range(len(v)):
	v[i] = int(v[i])

v.sort()

for i in range(len(v)):
	print(v[i], end=' ')
print()



