p = 9739
a = 497
b = 1768

def add(P,Q):
	if P == (0,0):
		return Q
	if Q == (0,0):
		return P
	if P[0]==Q[0] and P[1]==-Q[1]:
		return (0,0)
	if P==Q:
		l = ((3*P[0]**2+a)%p * pow(2*P[1],-1,p))%p
	else:
		l = ((Q[1]-P[1])%p * pow(Q[0]-P[0],-1,p))%p
	x3 = (l**2-P[0]-Q[0])%p
	y3 = (l*(P[0]-x3)-P[1])%p
	return (x3,y3)

P = (493, 5564)
Q = (1539, 4742)

print(add(P,Q))