# example of a pure function
from functools import reduce


def multiby2(li):
    newl = []
    for item in li:
        newl.append(item * 2)
    return newl


(multiby2([1, 3, 4]))


# map() -
mlist = [1, 2, 3, 4, 5, 6]
# ylist = [10, 23, 40]


def multiby3(item):
    return item**3


(list(map(multiby3, mlist)))


# filter()
def checkifodd(item):
    return item % 2 != 0


(list(filter(checkifodd, mlist)))
# zip() -


# print(list(zip(ylist, mlist)))
# reduce
def adder(ad, item):
    print(ad, item)
    return ad + item


(reduce(adder, mlist, 0))
(mlist)

# lambda expressions - functions wew only need to use once
# lambda param: action(param)
print(list(filter(lambda item: item % 2 != 0, mlist)))
