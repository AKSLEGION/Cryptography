from base64 import *

def hex_to_base64(hex_str):
	return b64encode(bytes.fromhex(hex_str)).decode()

#hex_str = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
#print(hex_to_base64(hex_str))

