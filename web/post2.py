
import requests
import json

host='http://web-09.challs.olicyber.it/login'
data={'username':'admin', 'password':'admin'}
x = requests.post(host, json=data)

print(x.text)
