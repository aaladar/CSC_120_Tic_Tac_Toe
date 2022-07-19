board = [['_', '_', '_'],
         ['_', '_', '_'],
         ['_', '_', '_']]


def playerOneMove():
    try:
        player_one_row = int(input("Player One... choose a row (0-2): "))
        player_one_column = int(input("Player One... choose a column (0-2): "))
        if board[player_one_row][player_one_column] != '_':
            print("Space already occupied! Please try again.")
            playerOneMove()
        else:
            board[player_one_row][player_one_column] = "X"
            print_board()
            if check_victory():
                print("Player One Wins!")
            elif check_tie():
                print("No more available moves. It's a tie!")
            else:
                playerTwoMove()
    except:
        print("Invalid entry! Please try again.")
        playerOneMove()


def playerTwoMove():
    try:
        player_two_row = int(input("Player Two... choose a row (0-2): "))
        player_two_column = int(input("Player Two... choose a column (0-2): "))
        if board[player_two_row][player_two_column] != '_':
            print("Space already occupied! Please try again.")
            playerTwoMove()
        else:
            board[player_two_row][player_two_column] = "O"
            print_board()
            if check_victory():
                print("Player Two Wins!")
            elif check_tie():
                print("No more available moves. It's a tie!")
            else:
                playerOneMove()
    except:
        print("Invalid entry! Please try again.")
        playerTwoMove()

def print_board():
    pass

def check_victory():
    pass

def check_tie():
    pass