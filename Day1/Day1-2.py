def main():
    data = import_data(path='input.txt')
    print(len(data))
    count = 0
    data = [int(d) for d in data.copy()]
    for i in range(3,len(data),1):
        if sum(data[i-2:i+1]) > sum(data[i-3:i]):
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