import json
import urllib.request

urlAddress = input('Enter location: ')
data = urllib.request.urlopen(urlAddress).read().decode()
print('Retrieving', urlAddress)

info = json.loads(data)

count = 0
sum = 0

for i in info['comments']:
      count += 1
      sum += int(i['count'])

print('Retrieved', len(data), 'characters')
print('Count:', count)
print('Sum:', sum)

