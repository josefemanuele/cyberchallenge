from pwn import *

flag = 'CCIT{s1d3_ch4nn3ls_'
conn = remote('benchmark.challs.cyberchallenge.it', 9031)

conn.recvuntil(':'.encode('utf-8'))
while True:
    max = 0
    char = ''
    for c in string.printable[0:-7]:
        conn.send((flag + c + '\n').encode('utf-8'))
        resp = conn.recvuntil(':'.encode('utf-8'))
        clocks = int(resp.decode('utf-8').split(' ')[4])
        if clocks > max:
            max = clocks
            char = c
    flag += char
    print(flag)

conn.close()
print(flag)
