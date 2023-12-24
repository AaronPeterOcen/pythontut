# Generators  is a function that returns an iterator
# using the Yield keyword. In this article
# Range is one of them


# A generator function that yields 1 for first time,
# 2 second time and 3 third time
def simpleGeneratorFun():
    yield 1
    yield 2
    yield 3


# Driver code to check above generator function
for value in simpleGeneratorFun():
    print(value)


# syntax of the generator
def generatorfunc(num):
    for i in range(num):
        # uses yield instead of return
        # it pauses the function until a condition is met
        yield i**i


# for it in generatorfunc(1000):
#     print(it)
# next cant be used if the range expires

g = generatorfunc(10)
next(g)
next(g)
next(g)
print(next(g))


# standard way to iterate
# def malelist(num):
#     res = []
#     for i in range(num):
#         res.append(i**i)
#     return res


# lists = malelist(100)
# print(list(range(1000)))

# under the hood of generators
