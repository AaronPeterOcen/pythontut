class Emp:
    # pass for empty
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@mymail.com"

        # printing the fullname

    def fullname(self):
        return "{} {}".format(self.first, self.last)


emp1 = Emp("Tyenn", "Peer", "30000")
emp2 = Emp("Bennth", "Arks", "34000")

print(emp1.email)
print(emp2.email)

print(emp1.fullname())
print(emp2.fullname())
