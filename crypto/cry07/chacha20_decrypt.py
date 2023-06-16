
import sys
from Cryptodome.Cipher import ChaCha20

key = bytes.fromhex(sys.argv[1])
ciphertext = bytes.fromhex(sys.argv[2])
nonce = bytes.fromhex(sys.argv[3])
cipher = ChaCha20.new(key=key, nonce=nonce)
plain = cipher.decrypt(ciphertext)
print(plain)
