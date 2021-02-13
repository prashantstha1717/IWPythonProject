# Write a Python program to get a string made of the first 2 and the last 2 chars
# from a given a string. If the string length is less than 2, return instead of the
# empty string.

# Sample String : 'Python'
# Expected Result : 'Pyon'
# Sample String : 'Py'
# Expected Result : 'PyPy'
# Sample String : ' w'
# Expected Result : Empty String


def out2(string):
    if len(string) > 2:
        x = string[:2]
        y = string[-2:]
        return x + y
    elif len(string) == 2:
        return string + string
    else:
        return "Empty string"


print(out2('Python'))
print(out2('Py'))
print(out2('w'))
