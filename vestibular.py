n = int(input())
respostas = input()
gabarito = input()

pontos = 0

for i in range(n):
	if respostas[i] == gabarito[i]:
		pontos = pontos + 1

print(pontos)

