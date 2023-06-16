from pwn import *
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad

host = 'spg.challs.cyberchallenge.it'
port = 9600
conn = remote(host, port)

with open('wordlist.txt', 'r') as wordlist:
    words = wordlist.readlines()

print("Generate passwords")
cipher = DES.new(key = b"\x00"*8, mode = DES.MODE_ECB)
passwords = list()
for word in words:
    word = word.strip()
    pwd = cipher.encrypt(pad(word.encode(), 8))
    passwords.append(pwd.hex()[:12])

print("Start brute forcing.")
conn.recv()
for password in passwords:
    conn.sendline(b'2')
    conn.recv()
    conn.sendline(b'admin')
    conn.recv()
    conn.sendline(password.encode())
    resp = conn.recv()
    if 'wrong' not in resp.decode():
        print(resp)
        break;
