# Write a Python program to print the even numbers from a given list.
# Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Expected Result : [2, 4, 6, 8]

sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def f10(sample):
    result = filter(lambda x: x % 2 == 0, sample)
    return result


print(list(f10(sample_list)))