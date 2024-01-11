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
        
letters_to_numbers = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 4,
    'F': 5,
    'G': 6,
    'H': 7
}

#computer create 5 ships
def create_ships(board):
    for ship in range(5):
        ship_row, ship_column = randint(0,7), randint(0,7)
        while board[ship_row][ship_column] == "X":
            ship_row, ship_column = get_ship_location()
        board[ship_row][ship_column] = "X"
        
