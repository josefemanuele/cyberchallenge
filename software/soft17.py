#!/usr/bin/env python3

# Importa la libreria di pwntools
from pwn import *


def main():
    '''
    remote(hostname, port) apre una socket e ritorna un object
    che può essere usato per inviare e ricevere dati sulla socket  
    '''
    HOST = "software-17.challs.olicyber.it"
    PORT = 13000
    r = remote(HOST, PORT)

    r.sendline(b"A")

    for i in range(10):
        data = r.recvuntil(b"somma questi numeri\n")
        print(data.decode())

        data = r.recvline()
        print(data.decode())
        array = data.decode().strip('[]\n').split(', ')
        sum = 0
        for n in array:
            sum += int(n)

        r.sendline(str(sum).encode())

    data = r.recvline()
    data = r.recvline()
    print(data.decode())


    # chiude la socket
    r.close()


if __name__ == "__main__":
    main()
