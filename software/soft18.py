#!/usr/bin/env python3

# Importa la libreria di pwntools
from pwn import *


def main():
    '''
    remote(hostname, port) apre una socket e ritorna un object
    che può essere usato per inviare e ricevere dati sulla socket  
    '''
    HOST = "software-18.challs.olicyber.it"
    PORT = 13001
    r = remote(HOST, PORT)

    r.sendline(b"A")

    for i in range(100):
        data = r.recvuntil(b'Step ')

        data = r.recvline()
        print(data.decode())
        array = data.decode().split()
        n = array[3]
        arch = array[6]
        if (arch[0] == '3'):
            out = p32(int(n, 16))
        else:
            out = p64(int(n, 16))

        r.send(out)

    data = r.recvline()
    data = r.recvline()
    print(data.decode())


    # chiude la socket
    r.close()


if __name__ == "__main__":
    main()
