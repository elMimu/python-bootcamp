def eh_primo(x):
	if x == 1 or x == 2:
		return False
	i = x - 1
	while i > 2:
		if(x%i == 0):
			return False
		i -= 1;
	
	return True
		

x = int(input())

if eh_primo(x):
	print('S')
else:
	print('N')
