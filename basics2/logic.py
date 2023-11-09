# if
is_old = True
is_driver = True
is_sober = True

if is_old and is_sober:
    print("you aint old enough and not sober")
elif is_driver:
    print("drive access")
else:
    print("naah")

# truthy && falsey
passwrd = "True"
# is_driver = True
name = "fibert"

# print(bool(5))
# print(bool())
if passwrd and name:
    print("user can continue")
# elif is_driver:
#     print("drive access")
else:
    print("enter password or usernamme to continue")

# Tenary Operator

# condtion_if_true if condition else condition_if_else
# [option1] if [condition] else [option2]
users = 50

print("all users online") if users >= 40 else print("waiting for other users")

# short_circuiting
is_user = True
is_password = False

if is_user and is_user:
    print("enter password")
    print(True)
