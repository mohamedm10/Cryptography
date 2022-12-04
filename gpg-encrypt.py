import gnupg
import os
gpg = gnupg.GPG(gnupghome="/home/runner/.gnupg")

path = './gpg_encrypt'
ptfile = '/my-data.txt'

with open(path+ptfile) as data:
    
    status = gpg.encrypt(data.read(),recipients=['ilyas@acme'], armor=False,)
  
with open(path+ptfile+'.encrypted', 'wb') as f: f.write(status.data)
  
print(status.ok)
print(status.stderr)