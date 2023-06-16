
import requests

host='http://web-08.challs.olicyber.it/login'
data={'username':'admin', 'password':'admin'}
x = requests.post(host, data=data)

print(x.text)
