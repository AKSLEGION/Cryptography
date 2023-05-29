def gcd(a, b):
	if (b == 0):
		return a
	else:
		return gcd(b, a % b)

def order(p, b):

	if (gcd(p, b) != 1):
		print("p and b are not co-prime.\n")
		return -1

	k = 3
	while (True):
		if (pow(b, k, p) == 1):
			return k
		k += 1

def convertx2e(x):
	z = 0
	while (x % 2 == 0):
		x = x / 2
		z += 1
		
	return [x, z]

def STonelli(n, p):
	if (gcd(n, p) != 1):
		print("a and p are not coprime\n")
		return -1
	if (pow(n, (p - 1) / 2, p) == (p - 1)):
		print("no sqrt possible\n")
		return -1
	ar = convertx2e(p - 1)
	s = ar[0]
	e = ar[1]
	q = 2
	while (True):
		if (pow(q, (p - 1) / 2, p) == (p - 1)):
			break
		q += 1
	x = pow(n, (s + 1) / 2, p)
	b = pow(n, s, p)
	g = pow(q, s, p)
	r = e
	while (True):
		m = 0
		while (m < r):
			if (order(p, b) == -1):
				return -1
			if (order(p, b) == pow(2, m)):
				break
			m += 1
		if (m == 0):
			return x
		x = (x * pow(g, pow(2, r - m - 1), p)) % p
		g = pow(g, pow(2, r - m), p)
		b = (b * g) % p

		if (b == 1):
			return x
		r = m
n=3
p=11
x = STonelli(n, p)
print("Modular square root of", n,"and", p, "is", x)
