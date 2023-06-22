

import requests

host='http://web-03.challs.olicyber.it/flag'
heads={'X-Password':'admin'}
x = requests.get(host, headers=heads)

print(x.text)
