from ECC_add import add

p = 9739
a = 497
b = 1768

def scalar_mult(P,n):
	R = (0,0)
	Q = P
	while n:
		if n&1:
			R = add(R,Q)
		Q = add(Q,Q)
		n //= 2
	return R

P = (2339,2213)
n = 7863

#print(scalar_mult(P,n))