# Write a Python program to get a string from a given string where all
# occurrences of its first char have been changed to '$', except the first char itself.

# Sample String : 'restart'
# Expected Result : 'resta$t'


def out3(string):
    x = string[0]  # first character of string
    string = string.replace(x, '$')
    string = x + string[1:]
    return string


print(out3('restart'))
