from cryptography.fernet import Fernet
import base64
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
# from cryptography.fernet import Fernet

def enter_pass():
    password_provided = input("Enter password")
    password = password_provided.encode()  # convert to type bytes
    salt = b'k\x84!^\xe6\xfa@8:\xc3\xbe\xe0p\xadF\xc7G'
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive(password))  # can only use kdf once
    return key

#open the file to encrypt
def encrypt_file(key):
    with open('test.txt', 'rb') as f:
        data = f.read()  # Read the bytes of the input file
    fernet = Fernet(key)
    encrypted = fernet.encrypt(data)
    #write the encrypted file
    with open('test.encrypted', 'wb') as f:
        f.write(encrypted) # Write the encrypted bytes to the output file
# Note: You can delete input_file here if you want

#decrypt file
def decrypt_file(key):
    input_file = 'test.encrypted'
    output_file = 'test.txt'

    with open(input_file, 'rb') as f:
        data = f.read()  # Read the bytes of the encrypted file

    fernet = Fernet(key)
    try:
        decrypted = fernet.decrypt(data)

        with open(output_file, 'wb') as f:
            f.write(decrypted)  # Write the decrypted bytes to the output file

        # Note: You can delete input_file here if you want
    except InvalidToken as e:
        print("Invalid Key - Unsuccessfully decrypted")
