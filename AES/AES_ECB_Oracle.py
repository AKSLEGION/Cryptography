import requests
from Crypto.Util.number import *
from Crypto.Util.Padding import pad

url = "https://aes.cryptohack.org/ecb_oracle/encrypt/"

padded_flag_len = 32
flag_len = 26
pad_len = padded_flag_len - flag_len
buf = "00"

flag = 'crypto{p3n6u1n5_h473_3cb}'

for i in range(len(flag)+1,flag_len+1):
    print(i)
    for j in "-!{}_0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
        print(j)
        checkflag = j + flag
        checkflag = pad(checkflag.encode(),16)
        payload = hex(bytes_to_long(checkflag))[2:] + buf*(pad_len+i+1)
        r=requests.get(url + payload)
        ct = eval(r.text.strip())["ciphertext"]
        if ct[:32] == ct[-32*(i//16+1):][:32]:
            flag = j + flag
            print(flag)
            break