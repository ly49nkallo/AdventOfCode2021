import numpy as np
def main():
    data = import_data(path='input2.txt')
    data = [y.strip().split() for x in [d.split('|') for d in data] for y in x]
    #filter out 1, 4, and 7, 8
    input_values = [data[i] for i in range(len(data)) if i % 2 == 0]
    output_values = [data[i] for i in range(len(data)) if i % 2 == 1]   
    print(output_values)
    nums = dict.fromkeys(range(10), 0)
    for row in output_values:
        for token in row:
            x = len(token)
            if x == 2:
                nums[1] += 1
            elif x == 4:
                nums[4] += 1
            elif x == 3:
                nums[7] += 1
            elif x == 7:
                nums[8] += 1
    print(nums)
    a = [nums[1], nums[4], nums[7], nums[8]]
    print(sum(a))

def import_data(path:str) -> list:
    data = list()
    with open(path, 'r') as f:
        data = f.readlines()
    assert isinstance(data, list)
    return data

if __name__ == '__main__':
    main()