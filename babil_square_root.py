def babil_square_root(a, eps):
	x0 = (1+a) / 2
	x1 = (x0+a/x0) * 0.5
	y = (x1-x0) / x0
	if y < 0:
		y = -y
	while y > eps:
		x0 = x1
		x1 = (x0+a/x0) * 0.5
		y = (x1-x0) / x0
		if y < 0:
			y = -y
	ret = "The square root of the number %s is %s" % (a, x1)
	print(ret)


def babil_square_root_main():
	babil_square_root(5,7)


babil_square_root_main()