# Write a Python program to find intersection of two given arrays using Lambda.

array1 = list(range(11))
array2 = list(range(5, 15))


def f20(a, b):
    result = list(filter(lambda x: x in a, b))
    return result


print(f20(array1, array2))