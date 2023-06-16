from Crypto.Cipher import AES
import binascii, sys

def xor(a, b):
    return bytes([x^y for x,y in zip(a, b)])

''''
KEY = "yn9RB3Lr43xJK2██".encode()
IV  = "████████████████".encode()
'''
msg = "AES with CBC is very unbreakable"
cipher = "c5██████████████████████████d49e78c670cb67a9e5773d696dc96b78c4e0"

k = "yn9RB3Lr43xJK2"
key = "yn9RB3Lr43xJK2tp"
B2 = bytes.fromhex(cipher[32:64])
A1 = msg[:16].encode()
A2 = msg[16:32].encode()

keys = [k.encode() + int(i).to_bytes() + int(j).to_bytes() for i in range(256) for j in range(256)]

decryptions = dict()
for k in keys:
    cipher = AES.new(k, AES.MODE_ECB)
    decryptions.update({cipher.decrypt(B2):cipher})

C1 = 0
B1 = 0
for d in decryptions:
    b = binascii.hexlify(xor(d, A2)).decode()
    if b[-4:] == 'd49e' and b[:2] == 'c5':
        print(b)
        B1 = xor(d, A2)
        C1 = decryptions[d]
    
IV = xor(C1.decrypt(B1), A1)
print(C1)
print(B1)
print(IV)

