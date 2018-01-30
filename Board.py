#Creating a testboard in order to test our functions/checkers.

#TODO: We probably need to create a board with "used" crosses (what we called circles before) in order to test the function test_if_complete_line.
def board_maker(size):
    board = [[0] * size for i in range(size)]
    # board[1][0] = 1


    # SmallSquare = 2
    # Bigsqure = o, a, b, c

    board[1][3] = 3
    board[1][5] = 3
    board[1][7] = 3
    board[3][1] = 2
    board[3][3] = 2
    board[3][5] = 6
    board[3][7] = 2
    board[3][9] = 2
    board[5][9] = 2
    board[7][1] = 2
    board[7][3] = 5
    board[7][7] = 5
    board[7][9] = 2
    board[9][7] = 2
    board[0][1] = 1
    board[0][5] = 1
    board[0][9] = 1
    board[1][0] = 1
    board[1][2] = 1
    board[1][4] = 1
    board[1][6] = 1
    board[1][8] = 1
    board[1][10] = 1
    board[2][3] = 1
    board[2][7] = 1
    board[3][0] = 1
    board[3][10] = 1
    board[4][1] = 1
    board[4][3] = 1
    board[4][7] = 1
    board[4][9] = 1
    board[5][4] = 1
    board[5][6] = 1
    board[6][1] = 1
    board[6][3] = 1
    board[6][7] = 1
    board[6][9] = 1
    board[7][0] = 1
    board[7][10] = 1
    board[8][5] = 1
    board[9][0] = 1
    board[9][4] = 1
    board[9][6] = 1
    board[9][10] = 1
    board[10][1] = 1
    board[10][3] = 1
    board[10][7] = 1
    board[10][9] = 1
    return board