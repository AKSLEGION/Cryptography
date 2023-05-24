import base64
from cryptography.hazmat.primitives.serialization import Encoding, PublicFormat
from cryptography.x509 import load_der_x509_certificate

# Load the DER-encoded certificate from a file
with open('rsa_key.der', 'rb') as f:
    der_data = f.read()

# Load the DER-encoded certificate using cryptography
cert = load_der_x509_certificate(der_data)

# Convert the certificate to PEM format
pem_data = cert.public_bytes(Encoding.PEM)

# Write the PEM-encoded certificate to a file
with open('rsa_key.pem', 'wb') as f:
    f.write(pem_data)

# Print the PEM-encoded certificate
print(pem_data.decode())