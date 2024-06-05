inp = int(input())
if inp == 1:
	print(1)
else:
	a = 0
	b = 1
	while True:
		a += b
		b += 1
		if inp // (a*6+2) == 0:
			break
	print(b)