def three_plus_one(x):
	i = 0
	while x > 1:
		++i
		if x % 2:
			x = 3*x+1
		else:
			x = x/2
		print(x)

def three_plus_one_main(x):
	three_plus_one(x)

three_plus_one_main(15000)