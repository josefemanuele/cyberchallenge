
import requests
from bs4 import BeautifulSoup

host='http://web-13.challs.olicyber.it/'
x = requests.get(host)

soup = BeautifulSoup(x.text, 'html.parser')

for i in soup.find_all('span', class_='red'):
    print(i.text, end='')
