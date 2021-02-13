# Write a Python program to convert a list to a tuple.

def out42(lis):
    return tuple(lis)


print(out42([1, 2, 3, 'a']))
print(type(out42([1, 2, 3, 'a'])))