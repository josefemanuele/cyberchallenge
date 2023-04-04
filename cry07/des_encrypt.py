
import sys
from Cryptodome.Cipher import DES
from Cryptodome.Util.Padding import pad

key = bytes.fromhex(sys.argv[1])
plaintext = 'La lunghezza di questa frase non è divisibile per 8'
cipher = DES.new(key, DES.MODE_CBC)
iv = cipher.iv.hex()
msg = cipher.encrypt(pad(plaintext.encode('utf-8'), 8, style='x923')).hex()
print( iv + ' ' + msg)
