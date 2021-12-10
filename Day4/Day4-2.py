import numpy as np
from functools import reduce
def main():
    data = import_data(path='input.txt')
    data = list(filter(lambda x: x != '\n', data))
    data = [d[:-1] for d in data]
    drawnNumbers = data[0]
    drawnNumbers = list(map(int, drawnNumbers.split(',')))
    print(drawnNumbers)
    boardData = data[1:]
    boardData = [d.split() for d in boardData]
    boardData = list(reduce(lambda x, y: x + y, boardData))
    boards = list()
    for i in range(25, len(boardData)+1, 25):
        boards.append(np.array(boardData[i-25:i]).reshape((5,5)).astype('int16'))
    masks = [np.ones(shape=(5,5)).astype('int16') for i in range(len(boards))]
    notWon = list(range(len(boards)))
    winningNum = None
    for num in drawnNumbers:
        for board in range(len(boards)):
            for j in range(5):
                for i in range(5):
                    if boards[board][i,j] == num:
                        masks[board][i, j] = 0
            if checkMask(masks[board]):
                try:
                    notWon.remove(board)
                except ValueError: pass
            if len(notWon) == 0:
                winningNum = num
                notWon = board
                break      
    
        if winningNum is not None: break
    if notWon is None:
        raise NameError('no winning index found')
    print(masks[notWon])
    # winningBoard contains the index of the winning board
    # find sum of all unmarked tiles
    s = sum(np.multiply(boards[notWon], masks[notWon]).flatten())
    print(s)
    s *= winningNum
    print(s)

def checkMask(mask:np.ndarray):
    for row in mask:
        if sum(row) == 0:
            return True
    for column in mask.T:
        if sum(column) == 0:
            return True
    return False

def import_data(path:str) -> list:
    data = list()
    with open(path, 'r') as f:
        data = f.readlines()
    assert isinstance(data, list)
    return data

if __name__ == '__main__':
    main()