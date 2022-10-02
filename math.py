# Division is decimal by default
print(5 / 2)
>>> 2.5

# Double slash rounds down
print(5 // 2)
>>> 2

# CAREFUL: most languages round towards 0 by default
# So negative numbers will round down
print(-3 // 2)
>>> -2

# A workaround for rounding towards zero
# is to use decimal division and then convert to int.
print(int(-3 / 2))
>>> -1

# Modding is similar to most languages
print(10 % 3)
>>> 1

# Except for negative values
print(-10 % 3)
>>> 2

# To be consistent with other languages modulo
import math
from multiprocessing import heap
print(math.fmod(-10, 3))
>>> -1

# More math helpers
print(math.floor(3 / 2))
>>> 1
print(math.ceil(3 / 2))
>>> 2
print(math.sqrt(2))
>>> 1.4142135623730951
print(math.pow(2, 3))
>>> 8

# Max / Min Int
float("inf")
float("-inf")

# Python numbers are infinite so they never overflow
print(math.pow(2, 200))
>>> 1.6069380442589903e+60

# But still less than infinity
print(math.pow(2, 200) < float("inf"))
>>> True