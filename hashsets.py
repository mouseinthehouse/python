# HashSet
mySet = set()

mySet.add(1)
mySet.add(2)
print(mySet)
>>> {1, 2}
print(len(mySet))
>>> 2

print(1 in mySet)
>>> True
print(2 in mySet)
>>> True
print(3 in mySet)
>>> False

mySet.remove(2)
print(2 in mySet)
>>> False

# list to set
print(set([1, 2, 3]))
>>> {1, 2, 3}

# Set comprehension
mySet = { i for i in range(5) }
print(mySet)
>>> {0, 1, 2, 3, 4}