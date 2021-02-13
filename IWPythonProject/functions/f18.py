# Write a Python program to check whether a given string is number or not using Lambda.

def f18(string):
    return string.isnumeric()


print(f18("123"))
print(f18("123abc"))
print(f18('abc123'))
print(f18("9812345678"))