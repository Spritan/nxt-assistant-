#intro
"""
    for encrypting/ decrypting passwords and confing files
"""
#imports
from getpass import getpass
from pbkdf2 import PBKDF2
from Crypto.Cipher import AES
import os
import base64
import pickle


### Settings ###

saltSeed = 'mkhgts465wef4fwtdd'  # MAKE THIS YOUR OWN RANDOM STRING

PASSPHRASE_FILE = './secret.p'
SECRETSDB_FILE = './secrets'
PASSPHRASE_SIZE = 64  # 512-bit passphrase
KEY_SIZE = 32  # 256-bit key
BLOCK_SIZE = 16  # 16-bit blocks
IV_SIZE = 16  # 128-bits to initialise
SALT_SIZE = 8  # 64-bits of salt


### System Functions ###

def getSaltForKey(key):
    # Salt is generated as the hash of the key with it's own salt acting like a seed value
    return PBKDF2(key, saltSeed).read(SALT_SIZE)


def encrypt(plaintext, salt):
    ''' Pad plaintext, then encrypt it with a new, randomly initialised cipher. Will not preserve trailing whitespace in plaintext!'''

    # Initialise Cipher Randomly
    initVector = os.urandom(IV_SIZE)

    # Prepare cipher key:
    key = PBKDF2(passphrase, salt).read(KEY_SIZE)

    cipher = AES.new(key, AES.MODE_CBC, initVector)  # Create cipher

    # Pad and encrypt
    return initVector + cipher.encrypt(plaintext + ' '*(BLOCK_SIZE - (len(plaintext) % BLOCK_SIZE)))


def decrypt(ciphertext, salt):
    ''' Reconstruct the cipher object and decrypt. Will not preserve trailing whitespace in the retrieved value!'''

    # Prepare cipher key:
    key = PBKDF2(passphrase, salt).read(KEY_SIZE)

    # Extract IV:
    initVector = ciphertext[:IV_SIZE]
    ciphertext = ciphertext[IV_SIZE:]

    # Reconstruct cipher (IV isn't needed for edecryption so is set to zeros)
    cipher = AES.new(key, AES.MODE_CBC, initVector)

    return cipher.decrypt(ciphertext).rstrip(' ')  # Decrypt and depad


### User Functions ###

def store(key, value):
    ''' Sore key-value pair safely and save to disk.'''
    global db

    db[key] = encrypt(value, getSaltForKey(key))
    with open(SECRETSDB_FILE, 'w') as f:
        pickle.dump(db, f)


def retrieve(key):
    ''' Fetch key-value pair.'''
    return decrypt(db[key], getSaltForKey(key))


def require(key):
    ''' Test if key is stored, if not, prompt the user for it while hiding their input from shoulder-surfers.'''
    if not key in db:
        store(key, getpass('Please enter a value for "%s":' % key))


### Setup ###

# Aquire passphrase:
try:
    with open(PASSPHRASE_FILE) as f:
        passphrase = f.read()
    if len(passphrase) == 0:
        raise IOError
except IOError:
    with open(PASSPHRASE_FILE, 'w') as f:
        passphrase = os.urandom(PASSPHRASE_SIZE)  # Random passphrase
        f.write(base64.b64encode(passphrase))

        try:
            # If the passphrase has to be regenerated, then the old secrets file is irretrievable and should be removed
            os.remove(SECRETSDB_FILE)
        except:
            pass
else:
    # Decode if loaded from already extant file
    passphrase = base64.b64decode(passphrase)

# Load or create secrets database:
try:
    with open(SECRETSDB_FILE) as f:
        db = pickle.load(f)
    if db == {}:
        raise IOError
except (IOError, EOFError):
    db = {}
    with open(SECRETSDB_FILE, 'w') as f:
        pickle.dump(db, f)

### Test (put your code here) ###
require('id')
require('password1')
require('password2')
print
print 'Stored Data:'
for key in db:
    # decode values on demand to avoid exposing the whole database in memory
    print key, retrieve(key)
    # DO STUFF
