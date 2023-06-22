
import requests
from bs4 import BeautifulSoup

host='http://web-12.challs.olicyber.it/'
x = requests.get(host)

soup = BeautifulSoup(x.text, 'html.parser')

print(soup.find_all('p'))
