#!usr/bin/python3
import random
number = random.randint(-10, 10)
print(number)
#Enter = int(input('Enter a number: '))
#print('user entered', Enter)
if number > 0:
    print('is positive')
elif number == 0:
    print('is zero')
else:
    print('is negative')