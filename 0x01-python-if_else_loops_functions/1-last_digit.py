#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    lastDigit = number % 10
else:
    lastDigit = ((number * -1) % 10) * -1
    
str = 'Last digit of {:d} is {:d} '
if lastDigit > 5:
    str = str + 'and is greater than 5'
elif lastDigit < 6:
    if lastDigit == 0:
        str = str + 'and is 0'
    else:
        str = str + 'and is less than 6 and not 0'
print(str.format(number, lastDigit))
