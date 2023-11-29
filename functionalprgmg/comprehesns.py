# list, set, dictionary
# compreshions are a quick way to create dictionary, list, set

# list
# list = [param for param in iterable]
mylist = [char for char in "my word!!!"]
mylist2 = [num for num in range(0, 100)]
# multiplyinh the nums by 2
mylist3 = [num**2 for num in range(0, 100)]
# getting even numbers only
mylist4 = [num**2 for num in range(0, 100) if num % 2 == 0]
# print(mylist)
# print(mylist4)

# set
# mylist = {char for char in "my word!!!"}
# mylist2 = {num for num in range(0, 100)}
# setdic = {"a": 2, "c": 5}
# mydic = {k: v * v for k, v in setdic.items() if v % 2 != 0}
mydic = {num: num**num for num in [1, 2, 3]}

print(mydic)
