from pwn import *

conn = remote('notadmin.challs.cyberchallenge.it', 9032)

delimitator = '>'
conn.recvuntil(delimitator.encode('utf-8'))
while True:
    for c in string.printable[0:-7]:
        conn.send(('1\n').encode('utf-8'))
        print(c)
        conn.recvuntil(':'.encode('utf-8'))
        conn.send((c + '\n').encode('utf-8'))
        token = conn.recvuntil(delimitator.encode('utf-8')).decode('utf-8').split(' ')[3].split('\n')[0]
        print(token)
        conn.send(('2\n').encode('utf-8'))
        conn.recvuntil(':'.encode('utf-8'))
        conn.send((token + '\n').encode('utf-8'))
        resp = conn.recvuntil('>'.encode('utf-8')).decode('utf-8')
        print(resp)

conn.close()
