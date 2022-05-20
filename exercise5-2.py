# Exercise 5.2
# 5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. 
# Once 'done' is entered, print out the largest and smallest of the numbers. 
# If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number. 
# Enter 7, 2, bob, 10, and 4 and match the output below.

largest = -99999999999999999999
smallest = 99999999999999999999
numbers = []

user = input("Enter a number: ").lower()
while user != 'done':
    try:
        num = int(user)
        numbers.append(num)
    except:
        print("Invalid input")
    user = input("Enter a number: ").lower()
        
for n in numbers:
    # Find Max
    if n >= largest:
        largest = n

    # Find Min
    if n <= smallest:
        smallest = n
            
print(f'Maximum is {largest}')
print(f'Minimum is {smallest}')