import re

# At least 8 char long
# contain any sort letters, nums $%@#

pattern = re.compile(r"^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$")

password = ('Pasasa123@')
password2 = ('aim12#')
a = pattern.search(password)
b = pattern.search(password2)

print(a)
print(b)

