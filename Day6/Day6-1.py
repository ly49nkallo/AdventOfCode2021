def main():
    data = import_data(path='input.txt')
    data = [int(d) for d in data[0].split(',')]
    current_state = data
    day = 0
    maxDays = 80
    while day < maxDays:
        # decerment each counter
        current_state = [i - 1 for i in current_state]
        # reset counters that have become -1 (were 0 at beginning of day)
        # track how many babies we need to append at the end
        newborns = 0
        for idx, v in enumerate(current_state):
            if v < 0:
                current_state[idx] = 6
                newborns += 1
        for i in range(newborns): 
            current_state.append(8)
        day += 1
    print(len(current_state))
    # CODE GOES HERE
    
def import_data(path:str) -> list:
    data = list()
    with open(path, 'r') as f:
        data = f.readlines()
    assert isinstance(data, list)
    return data

if __name__ == '__main__':
    main()