import requests
from Crypto.Util.number import *
from Crypto.Util.strxor import *

encrypt_url = 'https://aes.cryptohack.org/ecbcbcwtf/encrypt_flag/'
ciphertext = eval(requests.get(encrypt_url).text.strip())["ciphertext"]

encrypted_flag = [ ciphertext[i:i+32] for i in range(0,len(ciphertext),32) ]
iv = encrypted_flag[0]

flag = ''
decrypt_url = 'https://aes.cryptohack.org/ecbcbcwtf/decrypt/'
for i in range(len(encrypted_flag)-1,0,-1):
	encrypted_flag[i] = eval(requests.get(decrypt_url + encrypted_flag[i]).text.strip())["plaintext"]
	flag = long_to_bytes(int(encrypted_flag[i],16) ^ int(encrypted_flag[i-1],16)).decode() + flag
	
print(flag)