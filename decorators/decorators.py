# DECORATOR
# ability of functions to act like variables
# they super charge our functions
# wraps another function and enhances it or changes it
# adds extra functionality to other functions

# @decorator
# def hello():
#     pass


# Higher Order Function HOC -function that accepts another function / return another func
# def say(another):
#     another()

# # or

# def say2():
#     def another():
#         return 5
#     return another


def my_decorator(func):
    # decorator pattern
    def wrap_func(*a, **kw):
        print("///////")
        func(*a, *kw)
        print("///////")

    return wrap_func


@my_decorator
def hey(greeting="allo", emote=":-()"):
    print(greeting, emote)


# @my_decorator
# def nay():
#     print("alloo")


hey()
