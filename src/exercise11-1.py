# Exercise 11

import re

fileName = input("Enter file name: ")
fileHandler = open(fileName)

total = 0
numbers = re.findall('[0-9]+', fileHandler)
for number in numbers:
    total += int(number)
    
print(total)