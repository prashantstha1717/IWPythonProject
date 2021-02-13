# Write a Python program to multiplies all the items in a list.

from functools import reduce


def out17(func, lis):
    return func * lis


print(reduce(out17, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))