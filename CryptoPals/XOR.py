def xor(a,b):
	return hex(int(a,16)^int(b,16))[2:]

#a = '1c0111001f010100061a024b53535009181c'
#b = '686974207468652062756c6c277320657965'
#print(xor(a,b))