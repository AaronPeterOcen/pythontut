# DRY - Do not Repeat Yourself
# def tree():
#     pic = [
#         [0, 0, 0, 1, 0, 0, 0],
#         [0, 0, 1, 1, 1, 0, 0],
#         [0, 1, 1, 1, 1, 1, 0],
#         [1, 1, 1, 1, 1, 1, 1],
#         [0, 0, 0, 1, 0, 0, 0],
#         [0, 0, 0, 1, 0, 0, 0],
#     ]

#     for i in pic:
#         for p in i:
#             if p == 0:
#                 print(" ", end="")
#             elif p == 1:
#                 print("*", end="")
#         print("")


# tree()
# tree()


def hey():
    print("Hey!")


hey()


# parameters - used when we define the function
def hey_there(new, name):
    print(f"Hey! {new} {name}")


# arguments - used when we call the function
# hey_there("there", "Ocen")


# default parameters - give us a default value
def heythere(new, name="Ocen"):
    print(f"Hey! {new} {name}")


heythere("there")


# return - auto matically exits the function
# def sums(a, b):
#     return a + b
#     # print(add)


# def sum(a, b):
#     # doc string
#     """sum of

#     Args:
#         a (_type_): _description_
#         b (_type_): _description_
#     """

#     def adds(A, B):
#         return A + B

#     return adds(a, b)


# print(add)
# should do something really well
# should return somethng
# total = sum(5, 6)
# print(total)


# clean code
def is_even(num):
    return num % 2 == 0
    # eve = num % 2 == 0

    # if eve:
    #     return True
    # # else:
    # return False


print(is_even(3))

# *args **kwargs
# *args can take any number of args given to it
# *kwargs allow us to grab the kwargs and get a dictionary so tjhat we can access them


def superfn(*args, **kwars):
    # print(args)
    # a = sum(args)
    a = 0
    print(kwars)
    for items in kwars.values():
        a += items
    return sum(args) + a


print(superfn(1, 2, 3, 4, 5, num=1, num2=2))

# Rule: params, *args, default params, **kwargs


def hightesteven(li):
    a = 0
    for i in li:
        if i % 2 == 0:
            if i > a:
                a = i
    # print(a)
    return a


print(hightesteven([2, 4, 6, 8, 10]))

# walrus operator
#  :=
a = "iamfree"


def pr():
    if (n := len(a)) > 10:
        print(f"too long {n} elements")
    # return n


(pr())


# scope - what vars do i have access to

a = 1


def confusion():
    a = 5
    # return sum
    return a


print(a)
print(confusion())

total = 0


def count(total):
    total += 1
    return total


# print(count(4))
print(count(count(count(total))))

# rules
# start with local
# parent local
# global
# built in py functions


# nonlocal - usd to refer to the parent local
def outer():
    x = "local"

    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner:", x)

    inner()
    print("outer:", x)


outer()
