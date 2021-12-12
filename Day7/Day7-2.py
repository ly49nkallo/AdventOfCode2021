def main():
    data = import_data(path='input.txt')
    data = [int(d) for d in data[0].split(',')]
    # find average
    # CODE GOES HERE
    # 1+2+3+4...+n = (1 + n)/2 * n
    # = (abs(d-i) + 1) * abs(d-i) / 2
    print(min([sum([(abs(d - i)+1)*abs(d-i)/2 for d in data]) for i in range(len(data))]))
    
def import_data(path:str) -> list:
    data = list()
    with open(path, 'r') as f:
        data = f.readlines()
    assert isinstance(data, list)
    return data

if __name__ == '__main__':
    main()