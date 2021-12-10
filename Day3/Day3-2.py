import numpy as np
from functools import reduce
def main():
    data = import_data(path='input.txt')
    data = [list(d)[:-1] for d in data]
    data = np.array(data, dtype='int8')
    print(data)
    o2rating = list([d for d in data])
    i = 0
    while len(o2rating) > 1:
        # if the 1 bit is more common
        data = list(filter(lambda x: x[i] == int(sum(data.transpose()[i]) > data.shape[1] / 2),o2rating))
        i += 1
    print(o2rating)

def import_data(path:str) -> list:
    data = list()
    with open(path, 'r') as f:
        data = f.readlines()
    assert isinstance(data, list)
    return data

if __name__ == '__main__':
    main()