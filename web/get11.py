import requests
from bs4 import BeautifulSoup
import re

host='http://web-16.challs.olicyber.it/'

done = set()
new = set()
new.add(host)

while len(new) > 0:
    done.update(new)
    temp = set(new)
    new = set()
    for h in temp:
        x = requests.get(h)
        soup = BeautifulSoup(x.text, 'html.parser')
        finds = soup.find('h1', string=re.compile('.*flag{.*'))
        #finds = soup.find('h1')
        if finds is not None:
            print(finds)
        for e in soup.find_all('a'):
            external = host + e['href']
            if external not in done:
                new.add(external)

