
import requests
from bs4 import BeautifulSoup, Comment

host='http://web-14.challs.olicyber.it/'
x = requests.get(host)

soup = BeautifulSoup(x.text, 'html.parser')

for i in soup.find_all(string=lambda text: isinstance(text, Comment)):
    print(i)
