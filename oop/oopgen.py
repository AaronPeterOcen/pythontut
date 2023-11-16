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
    def shout(self):
        print(f"run away {self.name}")

    @classmethod  # standard is to use cls
    def add_stuff(cls, n1, n2):
        return cls("coc", n1 + n2)

    @staticmethod  # same as classmethod just not having accss to cls
    def add_stff(n1, n2):
        return n1 + n2


p3 = PlayerChar.add_stuff(2, 5)
print(p3.age)
player1 = PlayerChar("ocen", 13)
print(player1.add_stuff(1, 5))
