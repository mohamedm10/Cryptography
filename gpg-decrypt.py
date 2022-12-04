import gnupg
import os
gpg = gnupg.GPG(gnupghome="/home/runner/.gnupg")

path = './gpg_encrypt'
ptfile = '/my-data.txt.encrypted'

with open(path+ptfile,'rb') as data:

  status = gpg.decrypt(data.read(), passphrase = 'mypassphrase')
  

with open(path+ptfile+'.decrypted', 'wb') as f: f.write(status.data)
  
print(status.ok)
print(status.stderr)