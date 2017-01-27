from inspect import currentframe

def caller():
    data = [1, 2, 3]
    change_data()
    return data

def change_data():
    currentframe().f_back.f_locals["data"].append(5)

print(caller())
