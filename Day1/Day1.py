def main():
    data = import_data(path='input.txt')
    print(len(data))
    count = 0
    for i in range(len(data)):
        if data[i] > data[i-1]:
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