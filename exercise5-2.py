# Exercise 5.2
# 5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. 
# Once 'done' is entered, print out the largest and smallest of the numbers. 
# If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number. 
# Enter 7, 2, bob, 10, and 4 and match the output below.

largest = None
smallest = None
numbers = []

num = input("Enter a number: ")
while num.lower() != 'done':
    try:
        numbers.append(int(num))
    except:
        print("Invalid input")
    num = input("Enter a number: ")
        
for n in numbers:
    # Find Max
    if largest is None:
        largest = n
    elif n >= largest:
        largest = n

    # Find Min
    if smallest is None:
        smallest = n
    elif n <= smallest:
        smallest = n
            
print(f'Maximum is {largest}')
print(f'Minimum is {smallest}')