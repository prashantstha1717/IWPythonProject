# Write a Python program to add an item in a tuple.
tup = (1, 2, 3, 4)


def out40(*args):
    return tup + args


print(out40(10))
print(out40(10, 20, 30))
