from math import sqrt

n = int(input())

v = input().split()


for c in v:
	c = float(c)
	print("{:.4f}".format(sqrt(c)))	
