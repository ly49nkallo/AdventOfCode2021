import numpy as np

def main():
    data = import_data(path='input.txt')
    # CODE GOES HERE
    data = [d[:-1] for d in data]
    data = [d.split() for d in data]
    d = list()
    for line in data:
        d.append([line[0], line[2]])
    data = d
    d = list()
    for line in data:
        x = list()
        for string in line:
            x.append([int(string.split(',')[0]), int(string.split(',')[1])])
        d.append(x)
    data = d
    data = np.array(data, dtype='int16')
    world = np.zeros((max(max(data.T[0,0]), max(data.T[1,0]))+1, max(max(data.T[0,1]), max(data.T[1,1])+1)), dtype='int16')
    # ndarray clusterduck
    for line in data:
        if line[0,0] == line[1,0]:
            world[min(line[0,1], line[1,1]):min(line[0,1], line[1,1]) + abs(line[0,1] - line[1,1]) + 1, line[0,0]] += 1
        if line[0,1] == line[1,1]:
            world[line[0,1], min(line[0,0], line[1,0]):min(line[0,0],line[1,0]) + abs(line[0,0] - line[1,0]) + 1] += 1
    count = 0
    for i in range(len(world)):
        for j in range(len(world[0])):
            if world[i,j] >= 2:
                count += 1
    print(count)

def import_data(path:str) -> list:
    data = list()
    with open(path, 'r') as f:
        data = f.readlines()
    assert isinstance(data, list)
    return data

if __name__ == '__main__':
    main()