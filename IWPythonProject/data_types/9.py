# Write a Python program to change a given string to a new string where the first
# and last chars have been exchanged.

def out9(string):
    first_char = string[0]
    last_char = string[-1]
    final = last_char + string[1:-1] + first_char
    return final


print(out9('Insight Workshop'))
