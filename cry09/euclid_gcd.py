
import sys

def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        gcd, x, y = extended_gcd(b % a, a)
        return gcd, y - (b // a) * x, x

a = int(sys.argv[1])
b = int(sys.argv[2])
gcd, x, y = extended_gcd(a, b)
print(f'gcd= {gcd} x= {x} y= {y}')
