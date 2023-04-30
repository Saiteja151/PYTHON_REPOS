import example

example.add(3, 4)
example.add(90, 342)

print()

print(example.x)

print()

example.mul(5, 8)
example.mul(32, 47)

print()

import example as m

print(m.x)

print()

m.add(34, 45)
m.add(23, 67)

print()

m.mul(52, 81)
m.mul(57, 69)

print()

"""
from example import x, add

print(x)
add(10, 20)
mul(10, 30)         # NameError: name 'mul' is not defined
"""

from example import *

print(x)
add(10, 20)
mul(10, 20)

print()

""" Import Python Standard Library Modules """

import math

# use math.pi to get value of pi
print("The value of pi :", math.pi)

print()

""" Python import with Renaming """

import math as k

print(k.pi)

print()

""" Python from...import statement """

from math import pi

print(pi)

print()

""" Import all names """

# import all names from standard module math
from math import *

print("The value of pi is :", pi)

print()

import example

print(example.__name__)

print()

a = 1
b = "hello"

import math

print(dir())
