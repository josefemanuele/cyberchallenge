

import requests

host='http://web-04.challs.olicyber.it/users'
heads={'Accept':'application/xml'}
x = requests.get(host)
#x = requests.get(host, headers=heads)

print(x.text)
