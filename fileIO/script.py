# read, write, append

# my_file = open("test.txt")

# # print(my_file.read())
# print(my_file.readlines())

# my_file.close()

# OR
# to avoid using close
with open("test.txt", mode="r+") as my_file:
    # writing to a file
    text = my_file.write("Hola")
    # print(my_file.read())
    # print(my_file.readlines())
    print(text)

# using write to create a new file
with open("next.txt", mode="w") as my_file:
    text = my_file.write("Hola Da ma ste")
    print(text)

# file paths
with open("new/nxt.txt", mode="w") as my_file:
    text = my_file.write("Hola Da ma ste")
    print(text)

with open("new/nxt.txt", mode="r") as my_file:
    print(my_file.read())
