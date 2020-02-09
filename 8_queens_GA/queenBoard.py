import numpy as np

#print chess board with queens as 'O' and empty positions as '-'
def printBoard(formation, chromosomeSize):
    board = []
    for row in range(0, chromosomeSize):
        array = []
        for column in range(0, chromosomeSize):
            if row == formation[column]:
                array.append('O')
            else:
                array.append('-')
        board.append(array)

    print("board with current formation is:")
    print(np.matrix(board))
