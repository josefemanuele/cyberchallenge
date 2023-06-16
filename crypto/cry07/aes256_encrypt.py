
import sys
from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad

key = bytes.fromhex(sys.argv[1])
plaintext = 'Mi chiedo cosa significhi il numero nel nome di questo algoritmo.'
cipher = AES.new(key, AES.MODE_CFB, segment_size=24)
iv = cipher.iv.hex()
msg = cipher.encrypt(pad(plaintext.encode('utf-8'), 16, style='pkcs7')).hex()
print(msg + ' ' + iv)
