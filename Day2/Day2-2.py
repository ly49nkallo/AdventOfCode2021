def main():
    data = import_data(path='input.txt')
    print(len(data))
    horizontal = 0
    depth = 0
    aim = 0
    for d in data:
        command,x = d.split()
        x = int(x)
        if command == 'forward':
            horizontal += x
            depth += aim * x
        elif command == 'up':
            aim -= x
        elif command == 'down':
            aim += x
    print(horizontal, depth, horizontal*depth)


def import_data(path:str) -> list:
    data = list()
    with open(path, 'r') as f:
        data = f.readlines()
    assert isinstance(data, list)
    return data

if __name__ == '__main__':
    main()