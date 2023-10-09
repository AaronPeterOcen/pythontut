username = input("Enter username ")
password = input("Your password please ")
passwordlen = int(len(password))
hide = "*" * passwordlen

print(f"{username}, your password {hide} is {passwordlen} letters long")
