# formatted strings

name = "Ocen"
age = 22
print("Hi {}. you're {} years old".format("Ocen", 22))
print(f"Hi {name}. your {age} years old")

# sting indexing
nums = "01234567"
# [start:stop:stepover]
print(nums[::2])

# type conversion
birth_year = input("what year were you born?")
age = 2023 - int(birth_year)
print(f"your age is {age}")
