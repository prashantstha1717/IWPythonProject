# Write a Python program to create a function that takes one argument, and
# that argument will be multiplied with an unknown given number.

u_num = int(input("Enter a number that will be multiplied by argument: "))


def f12(num):
    return num * u_num


print(f12(3))