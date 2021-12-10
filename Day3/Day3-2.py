import numpy as np
from functools import reduce
def main():
    data = import_data(path='input.txt')      
    data = [list(d)[:-1] for d in data]
    data = np.array(data, dtype='int8')
    i = 0
    d = list(data)
    while i < len(data.T):
        mcb = 0
        if (sum(np.transpose(d)[i]) >= len(d) / 2):
            mcb = 1
        j = 0
        while j < len(d.copy()):
            if d[j][i] != mcb and len(d) > 1:
                d.pop(j)
                j -= 1
            j += 1
        i += 1
    assert len(d) == 1
    oxygenNum = 0
    for b in d[0]:
        oxygenNum = 2 * oxygenNum + b
    i = 0
    d = list(data)
    while i < len(data.T):
        mcb = 0
        if (sum(np.transpose(d)[i]) < len(d) / 2):
            mcb = 1
        j = 0
        while j < len(d.copy()):
            if d[j][i] != mcb and len(d) > 1:
                d.pop(j)
                j -= 1
            j += 1
        i += 1
    co2num = 0
    for b in d[0]:
        co2num = 2 * co2num + b
    print(oxygenNum, co2num, oxygenNum * co2num)

def import_data(path:str) -> list:
    data = list()
    with open(path, 'r') as f:
        data = f.readlines()
    assert isinstance(data, list)
    return data

if __name__ == '__main__':
    main()