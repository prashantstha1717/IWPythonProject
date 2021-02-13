# 1. Write a Python function to find the Max of three numbers.

def f1(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        max_num = num1
    elif num2 > num1 and num2 > num3:
        max_num = num2
    else:
        max_num = num3

    return max_num


print(f1(66, 333, 99))
