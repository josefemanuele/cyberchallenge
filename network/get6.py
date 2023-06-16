
import requests

host='http://web-06.challs.olicyber.it/token'
host2='http://web-06.challs.olicyber.it/flag'
s=requests.Session()
s.get(host)
x = s.get(host2)

print(x.text)
