import xml.etree.ElementTree as ET
import urllib.request

urlAddress = input('Enter location: ')
data = urllib.request.urlopen(urlAddress).read().decode()
print('Retrieving', urlAddress)

tree = ET.fromstring(data)
counts = tree.findall('.//count')

count = 0
sum = 0

for i in counts:
      count += 1
      sum += int(i.text)

print('Retrieved', len(data), 'characters')
print('Count:', count)
print('Sum:', sum)

