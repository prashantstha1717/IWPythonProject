# Write a Python program to remove a key from a dictionary

def out38(dic, key):
    del dic[key]
    return dic


dic = {1: 10, 2: 20, 3: 30}

print(out38(dic, 2))
