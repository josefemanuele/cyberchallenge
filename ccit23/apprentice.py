from Crypto.Hash import SHA3_384
import string

def enc(plain):
    res = b''
    for c in plain:
        res += SHA3_384.new(bytes([c])).digest()[:2]
    return res.hex()


def brute(b):
    for c in string.printable:
        c = c.encode()
        a = SHA3_384.new(c).digest()[:2]
        if a == b:
            return c.decode()
    print('not found')
    return ''

def dec(cypher):
    flag = ''
    res = bytes.fromhex(cypher)
    l = [res[2*i:2*(i+1)] for i in range(int(len(res) / 2))]
    for b in l:
        flag += brute(b)
    return flag

if __name__ == '__main__':
    with open('apprentice_output.txt', 'r') as rf:
        flag = rf.read().strip()

    print(dec(flag))

