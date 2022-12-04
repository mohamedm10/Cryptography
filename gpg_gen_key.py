import gnupg
import os
gpg=gnupg.GPG(gnupghome='/home/runner/.gnupg')

def gen_key():
  input_data = gpg.gen_key_input(
          name_email = 'ilyas@group83.com',
          passphrase = 'mypassphrase',
          key_type = 'RSA',
          key_length = 4096)
  
  
  key = gpg.gen_key(input_data)
  
  print(key)

gen_key()