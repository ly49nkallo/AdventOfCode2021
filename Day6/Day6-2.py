def main():
    data = import_data(path='input.txt')
    data = [int(d) for d in data[0].split(',')]
    days = [0] * 9
    #populate data
    for d in data:
            days[d] += 1
    for i in range(256):
        # cycle (i = 0,1,2,3,4,5,6,7,8)
        today = i % 9
        days[(today + 7) % 9] += days[today]
    print(sum(days))
    
    # CODE GOES HERE
    
def import_data(path:str) -> list:
    data = list()
    with open(path, 'r') as f:
        data = f.readlines()
    assert isinstance(data, list)
    return data

if __name__ == '__main__':
    main()