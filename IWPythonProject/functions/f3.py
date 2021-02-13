# Write a Python function to multiply all the numbers in a list.
# Sample List : (8, 2, 3, -1, 7)
# Expected Output : -336

from functools import reduce

sample_list = [8, 2, 3, -1, 7]


def f3():
    result = reduce(lambda a, b: a * b, sample_list)
    return result


print(f3())