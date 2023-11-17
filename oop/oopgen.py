# oop
#  class
# must use camel case
# blue print of whart we want to create

# class BigObj:
#     # code
#     pass
# obj1 = BigObj()
# print(type(obj1))


class PlayerChar:
    # constructor method
    # self allows us to have a reference to something that has not been created yet
    membership = True  # Class Obj Attribute

    def __init__(self, name, age):
        # if self.membership:  # or if PlayerChar.membership:
        self.name = name  # atributes
        self.age = age

    # method
    def run(self):
        print("run")

    # def shout(self, name):
    #     print(f"run away {name}")

    # @classmethod  # standard is to use cls
    # def add_stuff(cls, n1, n2):
    #     return cls("coc", n1 + n2)

    # @staticmethod  # same as classmethod just not having accss to cls
    # def add_stff(n1, n2):
    #     return n1 + n2

    # PILLARS OF OOP

    # encapsulation
    def shout(self):
        print(f"run away {self.name}")

    def tell(self):
        print(f"i am {self.name}")


# p3 = PlayerChar.add_stuff(2, 5)
# print(.age)
player1 = PlayerChar("ocen", 13)
player1.tell()

# Abstraction
# program to illustrate public access modifier in a class


# class Geek:
#     # constructor
#     def __init__(self, name, age):
#         # public data members
#         self.geekName = name
#         self.geekAge = age

#     # public member function
#     def displayAge(self):
#         # accessing public data member
#         print("Age: ", self.geekAge)


# # creating object of the class
# obj = Geek("R2J", 20)

# # accessing public data member
# print("Name: ", obj.geekName)

# # calling public member function of the class
# obj.displayAge()


# # program to illustrate private access modifier in a class


# class Geeks:
#     # private members
#     __name = None
#     __roll = None
#     __branch = None

#     # constructor
#     def __init__(self, name, roll, branch):
#         self.__name = name
#         self.__roll = roll
#         self.__branch = branch

#     # private member function
#     def __displayDetails(self):
#         # accessing private data members
#         print("Name: ", self.__name)
#         print("Roll: ", self.__roll)
#         print("Branch: ", self.__branch)

#     # public member function
#     def accessPrivateFunction(self):
#         # accessing private member function
#         self.__displayDetails()


# # creating object
# obj = Geeks("R2J", 1706256, "Information Technology")

# # calling public member function of the class
# obj.accessPrivateFunction()


# print(isinstance(wiz1, object))

# polymorphism
# for char in [wiz1, arch1]:
#     char.attack()


# Inheritance
class User:
    def __init__(self, email):
        self.email = email

    def signin(self):
        print("usr logged in")

    def attack(self):
        print("Attacking")


class Wizard(User):
    def __init__(self, name, power, email):
        # Super -allows us to refer to the User class without self
        super()
        self.name = name
        self.power = power

    def attack(self):
        print(f"usr attacking with power of {self.power}")


class Archer(User):
    def __init__(self, name, arrownum):
        self.name = name
        self.arrownum = arrownum

    def attack(self):
        print(f"usr attacking with arrows : arrows left-{self.arrownum}")


# introspection - what methpds i have access to

wiz1 = Wizard("Ocen", 30, "aar@h.com")
# arch1 = Archer("Ocen", 30)
# print(dir(wiz1))

# Dunder MEthods
# allows us to do some custom modifying of our classes


class Toy:
    def __init__(self, color, age):
        self.color = color
        self.age = age

    # modifying inbuilt methods
    def __str__(self):
        return f"{self.color}"

    def __len__(self):
        return 5


actionf = Toy("black", 13)
print(actionf.__str__())
print(str(actionf))
print(len(actionf))
