import sys
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
from Crypto.Signature import PKCS1_v1_5

def usage():
    print("Usage: \n"
            "digi-sig <priv-key> <data> <signature-file> <hash-file> \n")

if (len(sys.argv) < 5):
    usage()
    quit()

key_f = sys.argv[1]
data_f = sys.argv[2]
sig_f = sys.argv[3]
hash_f = sys.argv[4]

def generate_signature(key, data, sig_f, hash_f):
    print("Generating Signature")
    h = SHA256.new(data)
    rsa = RSA.importKey(key)
    signer = PKCS1_v1_5.new(rsa)
    signature = signer.sign(h)
    with open(sig_f, 'wb') as f: f.write(signature)
    print(h)
    # with open(hash_f, 'w') as f: f.write(h.digest())

# Read all file contents
with open(key_f, 'rb') as f: key = f.read()
with open(data_f, 'rb') as f: data = f.read()

if __name__ == "__main__":
    # Generate Signature
    generate_signature(key, data, sig_f, hash_f)
else:
    #Error
    usage()