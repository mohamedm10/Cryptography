import sys
from Crypto.PublicKey import RSA
# from Crypto.Hash import SHA256
from Crypto.Signature import PKCS1_v1_5

def usage():
    print("Usage: \n"
            "digi-sig <PUB-key> <data> <signature-file> <hash-file> \n")
  
if (len(sys.argv) < 4):
    usage()
    quit()

key_f = sys.argv[1]
sig_f = sys.argv[2]
hash_f = sys.argv[3]

def verify_signature(key, hash, sig_f):
    print("Verifying Signature")
    # h = SHA256.new(data)
    rsa = RSA.importKey(key)
    signer = PKCS1_v1_5.new(rsa)
    with open(sig_f, 'rb') as f: signature = f.read()
    rsp = "Success" if (signer.verify(hash, signature)) else " Verification Failure"
    print(rsp)

# Read all file contents
with open(key_f, 'rb') as f: key = f.read()
with open(hash_f, 'rb') as f: hash = f.read()

if __name__ == "__main__":
    # Verify Signature
    verify_signature(key, hash, sig_f)
else:
    #Error
    usage()