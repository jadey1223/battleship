from random import randint

#Board for holding ship locations
HIDDEN_BOARD = [[" "] * 10 for x in range(10)]
# Board for displaying hits and misses
GUESS_BOARD = [[" "] * 10 for i in range(10)]

def print_board(board):
    print("  A B C D E F G H I J")
    print("  *-*-*-*-*-*-*-*-*-*")
    row_number = 1
    for row in board:
        print("%d|%s|" % (row_number, "|".join(row)))
        row_number += 1