# error handling
# using a try block
try:
    age = int(input("age :->"))
    (age)
except:
    ("enter a number")

# or
while True:
    try:
        age = int(input("age :->"))
        10 / age
        # print(age)
    # to only accept valueError handling
    except ValueError:
        print("enter a number")
    except ZeroDivisionError:
        print("Please enter a non zero value")
    else:
        print("valid")
        break

# you can wrap the errors together to handle many errors
# except (TypeError, ZeroDivisionError)


def sun(n1, n2):
    try:
        return n1 / n2
    except (TypeError, ZeroDivisionError) as err:
        print(err)


print(sun(1, 0))
