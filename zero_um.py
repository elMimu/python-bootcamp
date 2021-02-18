a, b, c = input().split()

a = int(a)
b = int(b)
c = int(c)

if a == b and a == c:
	print("*")
elif a != b and b == c:
	print("A")
elif b != a and a == c:
	print("B")
else:
	print("C")


