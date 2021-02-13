# Write a Python program to remove an item from a tuple.

def out43(tup, index):
    convert_to_list = list(tup)
    convert_to_list.pop(index)
    return tuple(convert_to_list)


print(out43((1, 2, 3, 4), 2))


