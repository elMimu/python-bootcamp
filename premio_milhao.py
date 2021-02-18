n = int(input())
v = [] 

for i in range(n):
	temp = int(input())
	v.append(temp)

soma = 0
dias = 0

for elemento in v:
	if(soma < 1e+6):
		dias = dias + 1

	soma = soma + elemento

print(dias)
