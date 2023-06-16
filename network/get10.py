
import requests
from bs4 import BeautifulSoup
import re

host='http://web-15.challs.olicyber.it/'
x = requests.get(host)

soup = BeautifulSoup(x.text, 'html.parser')

ext = list()
for i in soup.find_all('link'):
    ext.append(i['href'])

for i in soup.find_all('script'):
    ext.append(i['src'])

for e in ext:
    x = requests.get(host+e)
    print(re.findall('flag{.+}', x.text))

