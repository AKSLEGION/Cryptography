def norm(v):
    ans=0
    for i in v:
        ans+=i**2
    return ans

def dot(v1,v2):
    ans=0
    for i in range(len(v1)):
        ans+=v1[i]*v2[i]
    return ans

def add(v1,a,v2,b):
    v=[0]*len(v1)
    for i in range(len(v1)):
        v[i]=a*v1[i]+b*v2[i]
    return v

def GLR(v1,v2):
    if(norm(v2)<norm(v1)):
        v1,v2=v2,v1
    m=dot(v1,v2)//norm(v1)
    if m==0:
        return v1,v2
    return GLR(v1,add(v2,1,v1,-m))

v = [846835985, 9834798552]
u = [87502093, 123094980]

print(GLR(v,u))