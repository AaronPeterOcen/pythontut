# Generators
# Range is one of them


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
