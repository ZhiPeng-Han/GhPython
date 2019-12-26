__author__ = "billpower"
__version__ = "2019.12.25"

import rhinoscriptsyntax as rs

number = list(range(10))
print(number)

a = number[3:6]
print(a)

b = number[-5:-1]
print(b)

c = number[4:]
print(c)
