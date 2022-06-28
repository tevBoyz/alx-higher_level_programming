#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    lastDigit = number % 10
else:
    lastDigit = ((number * -1) % 10) * -1
    
str1 = 'Last digit of {:d} is {:d} '
if lastDigit > 5:
    str1 = str1 + 'and is greater than 5'
elif lastDigit == 0:
    str1 = str1 + 'and is 0'
elif lastDigit < 6 and not 0:
    str1 = str1 + 'and is less than 6 and not 0'
print(str1.format(number, lastDigit))
