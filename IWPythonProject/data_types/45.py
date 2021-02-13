# Write a Python program to find the index of an item of a tuple

tup = (1, 2, 3, 'a', 'b', 'c')


def out45(ind):
    return tup.index(ind)


print(out45('a'))
print(out45(1))

