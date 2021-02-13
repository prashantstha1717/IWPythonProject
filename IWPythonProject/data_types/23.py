# Write a Python program to check a list is empty or not


def out23(lis):
    if bool(lis) is True:
        return "List is not empty"
    else:
        return "List is empty!!!"


print(out23([1, 'a', 3, 'd']))
print(out23([]))
