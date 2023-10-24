class Emp:
    # adding a variable
    raise_amount = 1.05
    num_emps = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@mymail.com"

        Emp.num_emps += 1

    def fullname(self):
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):
        # accessing the variable -> Emp or self
        self.pay = int(self.pay * self.raise_amount)

    # class methods
    # we work with the class instead of the instance
    @classmethod
    def set_raise_amt(cls, amt):
        cls.raise_amount = amt

    @classmethod
    def from_string(cls, empst):
        first, last, pay = empst.split("-")
        return cls(first, last, pay)


emp1 = Emp("Tyenn", "Peer", "30000")
emp2 = Emp("Bennth", "Arks", "34000")

# empstr1 = "Ocen-Aar-400"
# empstr2 = "Op-Ben-600"

# newempstr = Emp.from_string(empstr1)

# alternative constructors

# changing the raise amount value
# Emp.set_raise_amt(1.06)

# print(emp1.raise_amount)
# print(emp2.raise_amount)
