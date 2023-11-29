# square
mylist = [5, 4, 3]
(list(map(lambda item: item * item, mylist)))

# list sorting
a = [(0, 1), (4, 3), (2, 2), (5, 7), (9, -1)]
# using lambda to sort in the function
a.sort(key=lambda x: x[1])
print(a)
