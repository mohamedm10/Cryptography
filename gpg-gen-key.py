import gnupg
import os
gpg=gnupg.GPG(gnupghome='/home/runner/.gnupg')


input_data = gpg.gen_key_input(
        name_email = 'ilyas@acme.org',
        passphrase = 'mypassphrase',
        key_type = 'RSA',
        key_length = 1024)


key = gpg.gen_key(input_data)

print(key)