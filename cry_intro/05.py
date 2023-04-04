cypher = '104e137f425954137f74107f525511457f5468134d7f146c4c'

def xor(a, b):
    return bytes([x^y for x,y in zip(a, b)])

def brute_force(cypher):
    for key in range(256):
        a = key.to_bytes(1, 'big')
        for i in range(0, len(cypher), 2):
            b = bytes.fromhex(cypher[i] + cypher[i + 1])
            x = xor(a, b)
            print(x.decode('utf-8'), end='')
        print()

brute_force(cypher)
