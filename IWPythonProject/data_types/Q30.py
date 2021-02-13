# Write a Python script to check whether a given key already exists in a
# dictionary.

def out30(key, dic):
    if key in dic:
        print('Key already exists')
    else:
        print("Key doesn't exist")


out30(3, {1: 10, 2: 30, 3: 40})
out30(3, {1: 10, 2: 30})
