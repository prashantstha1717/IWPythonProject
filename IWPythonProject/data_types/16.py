# Write a Python program to sum all the items in a list

from functools import reduce


def out16(func, lis):
    return func + lis


print(reduce(out16, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
