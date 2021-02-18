def fatorial(x):
	if x == 0:
		return 1
	return x*fatorial(x -1)

N = int(input())
print(fatorial(N))
