from random import randint

#Initializing the gaming board
board = []

#Creating the 5x5 grid of Ocean
for x in range(5):
    board.append(["O"] * 5)

#To remove Commas and add spaces
def print_board(board):
    for row in board:
        print " ".join(row)

#Let the game begin!
print "-=Let's play Battleship!=-\n"
print_board(board)
print

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)

for turn in range(4):
    # Everything from here on should go in your for loop!
    # Be sure to indent four spaces!
    guess_row = int(raw_input("Guess Row:"))
    guess_col = int(raw_input("Guess Col:"))
    if guess_row == ship_row and guess_col == ship_col:
        board[guess_row][guess_col] = "#"
        print_board(board)
        print "\nCongratulations! You sunk my battleship!"
        break
        
    else:
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print "\nOops, that's not even in the ocean."
        elif(board[guess_row][guess_col] == "X"):
            print "\nYou guessed that one already."
        else:
            print "\nYou missed my battleship!"
            board[guess_row][guess_col] = "X"
        #Number of turns left are:
        print "\nTurn",turn+1
        print
        print_board(board)
        print
        if(turn==3):
            print "Game Over"