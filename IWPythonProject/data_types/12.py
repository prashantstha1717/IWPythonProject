# Write a Python script that takes input from the user and displays that input
# back in upper and lower cases.

def out12(string):
    print(string.upper())
    return string.lower()


print(out12(input('Type something: ')))