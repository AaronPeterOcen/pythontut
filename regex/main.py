import re

# great for validation
pattern = re.compile(r"([a-zA-Z]).([a])")
string = "I am the only man in the world"

# print("am" in string)
# searching using a regex
# returns None if the pattern is not found
a = pattern.search(string)
# b = pattern.findall(string)
# c = pattern.fullmatch(string)
# d = pattern.match(string)

# using the stored regex
# visit regex101.com
print(a)
