import numpy as np
from functools import reduce
def main():
    data = import_data(path='input.txt')
    data = [list(d)[:-1] for d in data]
    data = np.array(data, dtype='int8')
    gamma = np.zeros(shape=(data.shape[1],), dtype='int8')
    espilon = np.zeros(shape=(gamma.shape), dtype='int8')
    i = 0
    for column in data.transpose():
        if sum(column) > len(column) / 2:
            gamma[i] = 1
        else:
            espilon[i] = 1
        i += 1
    del i
    g = 0
    for b in gamma:
        g = 2 * g + b
    e = 0
    for b in espilon:
        e = 2 * e + b
    print (e * g)

def import_data(path:str) -> list:
    data = list()
    with open(path, 'r') as f:
        data = f.readlines()
    assert isinstance(data, list)
    return data

if __name__ == '__main__':
    main()