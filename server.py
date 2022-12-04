import sys
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
from Crypto.Signature import PKCS1_v1_5
import gnupg
import os
gpg = gnupg.GPG(gnupghome="/home/runner/.gnupg")

path = './gpg_encrypt/'
enc_file = 'my-data.txt.encrypted'
sig_file = 'my-data.txt.sig'

def usage():
    print("Usage: \n"
            "digi-sig <PUB-key> <encrypt-file> <signature-file> \n")
  
if (len(sys.argv) < 4):
    usage()
    quit()

key_f = sys.argv[1]
enc_f = path + sys.argv[2]
sig_f = path + sys.argv[3]

def verify_signature(key, data, sig_f):
    print("Verifying Signature")
    h = SHA256.new(data)
    rsa = RSA.importKey(key)
    signer = PKCS1_v1_5.new(rsa)
    with open(sig_f, 'rb') as f: signature = f.read()
    rsp = "Verification Success" if (signer.verify(h, signature)) else " Verification Failure"
    print(rsp)
    decrypt(data) if rsp == 'Verification Success' else 'Decryption Failure'

def decrypt(data):
  # with open(path+enc_f,'rb') as data: data = data.read()
  
  status = gpg.decrypt(data, passphrase = 'mypassphrase')
  
  with open(path+enc_file+'.decrypted', 'wb') as f: f.write(status.data)

  print('Decryption Successful')
  
# Read all file contents
with open(key_f, 'rb') as f: key = f.read()
with open(enc_f, 'rb') as f: data = f.read()
# with open('my-data.txt', 'rb') as f: data = f.read()

if __name__ == "__main__":
    # Verify Signature
    verify_signature(key, data, sig_f)
else:
    #Error
    usage()