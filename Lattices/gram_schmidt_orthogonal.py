def dot(a,b):
    v=0
    for i in range(len(a)):
        v+=a[i]*b[i]
    return v

def valsq(a):
    v=0
    for i in a:
        v+=i**2
    return v

v1 = [4,1,3,-1]
v2 = [2,1,-3,4]
v3 = [1,0,-2,7]
v4 = [6, 2, 9, -5]
v=[v1,v2,v3,v4]
u1 = v1
u=[u1]
nu=[0]*4
for i in range(3):
    u.append(nu[::])
mu=[]
for i in range(4):
    mu.append(nu[::])
for i in range(2,4+1):
    u[i-1]=v[i-1]
    for j in range(1,i):
        mu[i-1][j-1] = dot(v[i-1],u[j-1]) / valsq(u[j-1])
        for k in range(4):
            u[i-1][k]-=mu[i-1][j-1]*u[j-1][k]
print(u)