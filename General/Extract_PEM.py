#pip install PyCryptodome

from Crypto.PublicKey import RSA
from Crypto.IO import PEM

pem_data=open('rsa_key.pem','r').read()
pem_key,_,__=PEM.decode(pem_data)
rsa_key=RSA.import_key(pem_key)

#uncomment whichever key is required

#public_key=rsa_key.n
#print("public_key:",public_key)

#private_key=rsa_key.d
#print("private_key:",private_key)

exponent=rsa_key.e
print("exponent:",exponent)