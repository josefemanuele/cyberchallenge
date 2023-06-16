
import requests
import json

host='http://web-10.challs.olicyber.it/'
x = requests.options(host)
print(x.headers)
x = requests.patch(host)
print(x.headers)
x = requests.put(host)
print(x.headers)
