import numpy as np

def main():
    data = import_data(path='input.txt')
    data = [list(d.rstrip()) for d in data]
    
    for i in range(len(data)):
        for j in range(len(data[i])):
            data[i][j] = int(data[i][j])
    data = np.array(data).astype('uint8')
    print(data)
    print(data.shape)
    risk_level = 0
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            if isLow(i,j,data):
                risk_level += data[i,j] + 1
    print(risk_level)
def isLow(i, j, world:np.ndarray) -> bool:
    try: n = world[i-1,j]
    except IndexError: n = 10
    try: s = world[i+1,j]
    except IndexError: s = 10
    try: w = world[i,j-1]
    except IndexError: w = 10
    try: e = world[i,j+1]
    except IndexError: e = 10
    a = world[i,j]
    return a<n and a<w and a<s and a<e

def import_data(path:str) -> list:
    data = list()
    with open(path, 'r') as f:
        data = f.readlines()
    assert isinstance(data, list)
    return data

if __name__ == '__main__':
    main()