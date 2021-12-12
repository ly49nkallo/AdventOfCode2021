def main():
    data = import_data(path='input.txt')
    data = [int(d) for d in data[0].split(',')]
    # find average
    # CODE GOES HERE
    print(min([sum([abs(d - i) for d in data]) for i in range(len(data))]))
    
def import_data(path:str) -> list:
    data = list()
    with open(path, 'r') as f:
        data = f.readlines()
    assert isinstance(data, list)
    return data

if __name__ == '__main__':
    main()