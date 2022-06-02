# Exercise 9.4
# Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. 
# The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. 
# The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. 
# After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

##################################
# name = input("Enter file:")
# if len(name) < 1:
#    name = "mbox-short.txt"
# handle = open(name)
##################################

fileName = input("Enter file: ")
if len(fileName) < 1:
    fileName = "mbox-short.txt"

fileHandler = open(fileName)

fileAddress = dict()

for line in fileHandler:
    if 'From ' in line:
        splitLine = line.split()
        emailAddress = splitLine[1]
        if emailAddress in fileAddress:
            fileAddress[emailAddress] = fileAddress[emailAddress] + 1
        else:
            fileAddress[emailAddress] = 1

mostUsed = None
maxAmount = None

for address in fileAddress:
    if mostUsed is None and maxAmount is None:
        mostUsed = address
        maxAmount = fileAddress[address]
    elif fileAddress[address] > maxAmount:
        mostUsed = address
        maxAmount = fileAddress[address]

print(f'{mostUsed} {maxAmount}')