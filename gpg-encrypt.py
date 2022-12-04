import gnupg
import os
gpg = gnupg.GPG(gnupghome="/home/runner/.gnupg")

path = './gpg_encrypt'
ptfile = '/my-data.txt'

with open(path + ptfile) as data:
    
    status = gpg.encrypt_file(data,recipients=["ilyas@acme.org"],output=path+ptfile+'.encrypted')

print(status.ok)
print(status.stderr)