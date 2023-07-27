import requests
from Crypto.Util.number import *
from Crypto.Util.strxor import *

encrypt_url = 'https://aes.cryptohack.org/symmetry/encrypt_flag/'
ciphertext = eval(requests.get(encrypt_url).text.strip())["ciphertext"]
iv , ciphertext = ciphertext[:32] , ciphertext[32:]
decrypt_url = 'https://aes.cryptohack.org/symmetry/encrypt'
flag = bytes.fromhex(eval(requests.get(decrypt_url + '/' + ciphertext + '/' + iv).text.strip())["ciphertext"]).decode()
print(flag)