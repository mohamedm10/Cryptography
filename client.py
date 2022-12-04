import sys
import pickle
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
from Crypto.Signature import PKCS1_v1_5

def usage():
    print("Usage: \n"
            "digi-sig <priv-key> <data> <signature-file> \n")

if (len(sys.argv) < 4):
    usage()
    quit()

key_f = sys.argv[1]
data_f = sys.argv[2]
sig_f = sys.argv[3]

def generate_signature(key, data, sig_f):
    print("Generating Signature")
    h = SHA256.new(data)
    rsa = RSA.importKey(key)
    signer = PKCS1_v1_5.new(rsa)
    signature = signer.sign(h)
    with open(sig_f, 'wb') as f: f.write(signature)

# Read all file contents
with open(key_f, 'rb') as f: key = f.read()
with open(data_f, 'rb') as f: data = f.read()

if __name__ == "__main__":
    # Generate Signature
    generate_signature(key, data, sig_f)
else:
    #Error
    usage()