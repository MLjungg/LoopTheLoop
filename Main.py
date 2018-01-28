from checkers import *
from Board import board_maker

target_count = 3
start = 1
size = 11
board = board_maker(size)

for i in range(size):
    print (board[i])

check_if_one_loop(board, None, board.index(2))