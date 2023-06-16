import requests

host = 'http://10.20.30.40:37005/'
page = 'random'
random_array = [1792, 1313, 3480, 1151, 1302, 1582, 9311, 3741, 1358, 1049, 1254, 1732, 1289, 1524, 8608, 1986, 1289, 7144, 1585, 1487]

i = 0
resp = 'fool'
while 'fool' in resp:
    i += 1
    random = random_array[i%len(random_array)]
    x = requests.post(host + page, data=str(random))
    resp = x.text

print(resp)

