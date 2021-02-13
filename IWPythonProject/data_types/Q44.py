# Write a Python program to slice a tuple.

tup = (1, 2, 3, 4, 5, 6, 7)


def out44(start, end=-1):
    result = tup[start: end]
    return result


print(out44(0))
print((out44(1, 3)))
