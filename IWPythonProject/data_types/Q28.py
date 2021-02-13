# Write a Python script to add a key to a dictionary.
# Sample Dictionary : {0: 10, 1: 20}
# Expected Result : {0: 10, 1: 20, 2: 30}

sample = {0: 10, 1: 20}


def out28(key, value):
    sample[key] = value
    return sample


print(out28(2, 30))
