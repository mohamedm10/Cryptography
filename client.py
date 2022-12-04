import sys
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
from Crypto.Signature import PKCS1_v1_5
import gnupg
import os
from gpg_gen_key import gen_key

gpg = gnupg.GPG(gnupghome="/home/runner/.gnupg")

path = './gpg_encrypt'
ptfile = '/my-data.txt'

# generates key pair
gen_key()

def usage():
    print("Usage: \n"
            "digi-sig <priv-key> <data> \n")

if (len(sys.argv) < 3):
    usage()
    quit()

key_f = sys.argv[1]
data_f = sys.argv[2]

def encrypt(data):
  # with open(path+ptfile) as data: data = data.read()
    
  status = gpg.encrypt(data,recipients=['ilyas@group83.com'], armor=False,)
  
  with open(path+ptfile+'.encrypted', 'wb') as f: f.write(status.data)

def generate_signature(key, enc_f):
    print("Generating Signature")
    h = SHA256.new(enc_f)
    rsa = RSA.importKey(key)
    signer = PKCS1_v1_5.new(rsa)
    signature = signer.sign(h)
    with open(path+ptfile+'.sig', 'wb') as f: f.write(signature)

# Read all file contents
with open(key_f, 'rb') as f: key = f.read()
with open(data_f, 'rb') as f: data = f.read()

if __name__ == "__main__":
    # Generate Signature
    encrypt(data)
    with open(path+ptfile+'.encrypted', 'rb') as f: enc_f = f.read()
    generate_signature(key, enc_f)
else:
    #Error
    usage()