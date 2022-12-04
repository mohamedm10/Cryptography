import gnupg
import os
gpg = gnupg.GPG(gnupghome="/home/runner/.gnupg")

path = './gpg_encrypt'
ptfile = '/my-data.txt.encrypted'

with open(path + ptfile,'rb') as data:
    
    status = gpg.decrypt_file(data, passphrase = 'mypassphrase',output=path+ptfile+'.decrypted')

print(status.ok)
print(status.stderr)