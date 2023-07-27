import requests
from Crypto.Util.number import *

cookie_url = 'https://aes.cryptohack.org/flipping_cookie/get_cookie'
ciphertext = eval(requests.get(cookie_url).text.strip())["cookie"]
cookie = ciphertext[32:]
ciphertext = [ ciphertext[i:i+32] for i in range(0,len(ciphertext),32) ]
iv = ciphertext[0]
iv = hex( int(iv,16) ^ bytes_to_long(b'admin=False;expi') ^ bytes_to_long(b'admin=True;_____') )[2:]
decode_url = 'https://aes.cryptohack.org/flipping_cookie/check_admin'
flag = eval(requests.get(decode_url + '/' + cookie + '/' + iv).text.strip())["flag"]
print(flag)