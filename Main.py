from checkers import *
from Board import board_maker

def test():
    target_count = 3
    start = 1
    size = 11
    board = board_maker(size)

    for i in range(size):
        print (board[i])

    check_surrounding(board, size, target_count, start)

    check_if_complete_line(board, None, board.index(2))

def main():
    test()

main()
