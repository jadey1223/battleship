from random import randint

"""
----- Welcome to BATTLESHIPS -----

How to play:

1. There will be eight ships of varying length arranged at random across a 10 by 10 grid.
2. You will have 15 turns to sink all ships.
3. You can designate where to shoot by selecting a row and column, like A1.
4. For every shot that hits or misses it will show up in the grid.
5. A ship cannot be placed diagonally, so if a shot hits the rest of the ship is in one of 4 directions, left, right up, and down.

 Legend:
 
    1. " " = water or empty space
    2. "O" = Indicator that you missed the target
    3. "X" = part of ship that was hit with bullet

"""

#Board for holding ship locations
HIDDEN_BOARD = [[" "] * 9 for x in range(9)]
# Board for displaying hits and misses
GUESS_BOARD = [[" "] * 9 for i in range(9)]

#players Name request
print('what is your player name?')
user_name = input()
print('Welcome to Battleships {}!'.format(user_name))

#Creates grid 
def print_board(board):
    print(" A B C D E F G H I J")

def print_board(board):
    print("----------------------")
    print("      Battleship"      )
    print("----------------------")
    print("  A B C D E F G H I J")
    print("  ===================")
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
    'H': 7,
    'I': 8,
    'J': 9
}

#computer create 5 ships
def create_ships(board):
    for ship in range(5):
        ship_row, ship_column = randint(0,7), randint(0,7)
        while board[ship_row][ship_column] == "X":
            ship_row, ship_column = get_ship_location()
        board[ship_row][ship_column] = "X"
        
def get_ship_location():
    row = input("Enter the row of the ship: ").upper()
    while row not in "0123456789":
        print('Not an appropriate choice, please select a valid row')
        row = input("Enter the row of the ship: ").upper()
    column = input("Enter the column of the ship: ").upper()
    while column not in "ABCDEFGHIJK":
        print('Not an appropriate choice, please select a valid column')
        column = input("Enter the column of the ship: ").upper()
    return int(row) - 1, letters_to_numbers[column]

#check if all ships are hit
def count_hit_ships(board):
    count = 0
    for row in board:
        for column in row:
            if column == "X":
                count += 1
    return count

# A place marker if you hit or miss
if __name__ == "__main__":
    create_ships(HIDDEN_BOARD)
    turns = 15
    while turns > 0:
        print('Guess a battleship location')
        print_board(GUESS_BOARD)
        row, column = get_ship_location()
        if GUESS_BOARD[row][column] == "-":
            print("You guessed that one already.")
        elif HIDDEN_BOARD[row][column] == "X":
            print("--------------------")
            print("You Hit! Do it again")
            print("--------------------")
            GUESS_BOARD[row][column] = "X" 
            turns -= 1  
        else:
            print("----------------------------")
            print("You missed! Thats unforunate")
            print("----------------------------")
            GUESS_BOARD[row][column] = "O"   
            turns -= 1     
        if count_hit_ships(GUESS_BOARD) == 5:
            print("You win!")
            break
        print("You have " + str(turns) + " turns left")
        if turns == 0:
            print("Better luck next time :(")

letters_to_numbers = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 4,
    'F': 5,
    'G': 6,
    'H': 7,
    'I': 8,
    'J': 9,
    
}

#computer create 5 ships
def create_ships(board):
    for ship in range(5):
        ship_row, ship_column = randint(0,7), randint(0,7)
        while board[ship_row][ship_column] == "X":
            ship_row, ship_column = get_ship_location()
        board[ship_row][ship_column] = "X"
        
def get_ship_location():
    row = input("Enter the row of the ship: ").upper()
    while row not in "123456789":
        print('Not an appropriate choice, please select a valid row')
        row = input("Enter the row of the ship: ").upper()
    column = input("Enter the column of the ship: ").upper()
    while column not in "ABCDEFGHIJK":
        print('Not an appropriate choice, please select a valid column')
        column = input("Enter the column of the ship: ").upper()
    return int(row) - 1, letters_to_numbers[column]

#check if all ships are hit
def count_hit_ships(board):
    count = 0
    for row in board:
        for column in row:
            if column == "X":
                count += 1
    return count


            
    