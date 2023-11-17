class SuperList(list):
    def __init__(self):
        pass

    def __len__(self):
        return 100


superl = SuperList()

print(len(superl))
superl.append(3)
print(superl[0])
