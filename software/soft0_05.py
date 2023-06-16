#!/usr/bin/env python3

# Importa la libreria di pwntools
from pwn import *


def main():
    '''
    remote(hostname, port) apre una socket e ritorna un object
    che può essere usato per inviare e ricevere dati sulla socket  
    '''
    HOST = "piecewise.challs.cyberchallenge.it"
    PORT = 9110
    r = remote(HOST, PORT)

    while(True):
        data = r.recvline()
        print(data)

        request = str(data).split()
        if len(request) < 4:
            continue;
        if request[4] == "empty":
            out = b"\n"
        elif request[4] == "number":
            number = int(request[5])
            architecture = request[8].split('-')[0]
            endianness = request[9].split('-')[0]
            if architecture == "32":
                out = p32(number, endian=endianness)
            else:
                out = p64(number, endian=endianness)
        else:
            print("could not parse request ")

        print("sending " + str(out))
        r.send(out)

    # chiude la socket
    r.close()


if __name__ == "__main__":
    main()
