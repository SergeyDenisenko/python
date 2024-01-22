import random
import pandas as pd

lst = ['robot'] * 10
lst += ['human'] * 10
lst += ['pet'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})

def get_one_hot(data):
    names = data.unique()
    table = list()
    
    for elem in data:
        row = dict()
        for name in names:
            if elem == name:
                row[name] = 1
            else:
                row[name] = 0
        table.append(row)
    return pd.DataFrame(table)

print(get_one_hot(data['whoAmI']))