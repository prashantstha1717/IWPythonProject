# Write a Python function that takes a list and returns a new list with unique
# elements of the first list.
# Sample List : [1,2,3,3,3,3,4,5]
# Unique List : [1, 2, 3, 4, 5]


sample_list = [1, 2, 3, 3, 3, 3, 4, 5]


def f8(lis):
    return list(set(lis))


print(f8(sample_list))