import signal
from binascii import hexlify
from string import printable
from random import randint
from Cryptodome.Cipher import AES
from itertools import permutations

BLOCK = 16

#perms = [''.join(p) for p in permutations(printable[0:-8], BLOCK)]
print(permutations(printable[0:-8], 16))
