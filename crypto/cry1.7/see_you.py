#!/usr/bin/python3

import string
import base64
from itertools import product

#from secret import KEY

def encrypt(clear, key):
  enc = []
  for i in range(len(clear)):
    key_c = key[i % len(key)]
    enc_c = chr((ord(clear[i]) + ord(key_c)) % 128)
    enc.append(enc_c)   
  return str(base64.urlsafe_b64encode("".join(enc).encode('ascii')), 'ascii')

# For debug purpose
def decrypt(enc, key):
    dec = []
    enc = str(base64.urlsafe_b64decode(enc.encode('ascii')), 'ascii')
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((128 + ord(enc[i]) - ord(key_c)) % 128)
        dec.append(dec_c)
    return "".join(dec)
    #return str(base64.urlsafe_b64encode("".join(dec).encode('ascii')), 'ascii')
 
#assert(len(KEY) == 8)
#assert(all(c in string.ascii_lowercase for c in KEY))

m = "See you later in the city center"
c = "QSldSTQ7HkpIJj9cQBY3VUhbQ01HXD9VRBVYSkE6UWRQS0NHRVE3VUQrTDE="
key_space = string.ascii_lowercase

encs = dict()
decs = dict()
     
for k in product(key_space, repeat=4):
    key = ''.join(k)
    enc = encrypt(m, key)
    encs.update({enc : key})
    dec = decrypt(c, key)
    decs.update({dec : key})

for a in encs.keys():
    b = decs.get(a)
    if b is not None:
        KEY = encs.get(a) + b
        print("flag: CCIT{%s}" % KEY)

print('Done')
