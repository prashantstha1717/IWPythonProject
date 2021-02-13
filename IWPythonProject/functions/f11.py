# Write a Python program to create a lambda function that adds 15 to a given
# number passed in as an argument, also create a lambda function that multiplies
# argument x with argument y and print the result.

def f11():
    return lambda num: num + 15


add15 = f11()
print(add15(10))


def multiplier():
    return lambda x, y: x * y


mul = multiplier()
print(mul(2, 5))
