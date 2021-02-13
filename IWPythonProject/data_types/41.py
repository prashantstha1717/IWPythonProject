# Write a Python program to convert a tuple to a string.

tup = ('a', 'p', 'p', 'l', 'e')


def out41():
    string = "".join(tup)
    return string


print(out41())
print(type(out41()))