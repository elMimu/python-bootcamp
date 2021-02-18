risada = input()
tam = int(len(risada))

esquerda = ''
direita = ''

for char in risada:
	if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
		esquerda = esquerda + char

for i in range(tam - 1, -1, -1):
	if risada[i] == 'a' or risada[i] == 'e' or risada[i] == 'i' or risada[i] == 'o' or risada[i] == 'u':
		direita = direita + risada[i]	

if direita == esquerda:
	print('S')
else:
	print ('N')
	
