# check for duplicate in the list
some_list = ["a", "b", "c", "b", "d", "n", "m", "n"]
# print(len(some_list))
# list = set(some_list)
# print(len(list))

dups = []

for value in some_list:
    if some_list.count(value) > 1:
        if value not in dups:
            dups.append(value)

print(dups)
