# Write a Python function to sum all the numbers in a list.
# Sample List : (8, 2, 3, 0, 7)
# Expected Output : 20

from functools import reduce

sample_list = [8, 2, 3, 0, 7]


def f2():
    result = reduce(lambda a, b: a+b, sample_list)
    return result


print(f2())