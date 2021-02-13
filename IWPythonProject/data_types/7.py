# Write a Python function that takes a list of words and returns the length of the
# longest one.


def out7(lis):
    result = []
    for char in lis:
        length = len(char)
        result.append(length)
    return max(result)


print(out7(['apple', 'ball', 'cat', 'dog', 'elephant', 'zebra']))
