# Data Structs

# lists
l1 = [1, 2, 3, 4, 5, "a", "b", True]
l2 = ["a", "b", True]

# accessing items
print(l1[3])
print(l1[::3])

l1[0] = "c"
l3 = l1
l3[0] = 4
print(l3)
print(l1)

# listmethods
# adding
l3.append(100)
l3.insert(3, 99)
print(l3)

# removing
l3.pop()
l3.remove(True)
# clear
print(l3)

# range
print((list(range(100))))

# list unpacking
a, b, c = [1, 2, None]

print(a)
print(b)
print(c)

# None
None

print("end list\n")

# Dictionaries
# not sorted
# must have unique keys
dictionat = {"a": [1, 2, 3], "b": "xoxo", "c": False}

print(dictionat["b"])
print(dictionat["a"][2])

print(dictionat.get("d", "abos"))

print(dict(name="ocece"))

# use in to check for values
print("name" in dictionat)

# cant use booleans

# Tuple
# unchangeale lists

mtuple = (1, 2, 3)
# are also valid keys
# only 2 methods
mytuple = (1, 2, 3, 4, 5)
# print(mytuple.count())
# len()

# set
# unordered collection of unique objects
# myset = {1, 2, 3, 4, 5, 4, 5}
# print(myset)
# list = ["a", "b", "c", "d", "a"]
# print(set(list))

myset = {1, 2, 3, 4, 5, 4, 5}
set2 = {7, 6, 8, 9, 11}

print(myset.difference(set2))
