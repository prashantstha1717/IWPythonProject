# Write a Python script to concatenate following dictionaries to create a new
# one.
# Sample Dictionary :
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

def out29(dic1, dic2, dic3):
    dic1.update(dic2)
    dic1.update(dic3)
    return dic1


dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

print(out29(dic1, dic2, dic3))
