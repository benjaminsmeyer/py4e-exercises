# Exercise 10.2
# 10.2 Write a program to read through the mbox-short.txt and 
# figure out the distribution by hour of the day for each of the messages. 
# You can pull the hour out from the 'From ' line by finding the time and 
# then splitting the string a second time using a colon.
############ From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, 
# print out the counts, sorted by hour as shown below. 

##################################
# name = input("Enter file:")
# if len(name) < 1:
#     name = "mbox-short.txt"
# handle = open(name)
##################################

fileName = input("Enter file name: ")
if len(fileName) < 1:
    fileName = "mbox-short.txt"
fileHandler = open(fileName)

hourCount = dict()
for line in fileHandler:
    if 'From ' in line:
        # Gets Hour from Line
        hour = line.split()[-2].split(':')[0]
        hourCount[hour] = hourCount.get(hour, 0) + 1

for hourTime, timeCount in sorted(hourCount.items()):
    print(hourTime, timeCount)