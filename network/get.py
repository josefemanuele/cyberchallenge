

import requests

host='http://web-01.challs.olicyber.it/'
x = requests.get(host)

print(x.text)
