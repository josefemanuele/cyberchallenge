

import requests

host='http://web-02.challs.olicyber.it/server-records'
pars={'id':'flag'}
x = requests.get(host, params=pars)

print(x.text)
