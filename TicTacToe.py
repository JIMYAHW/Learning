board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
gameOn = True
winner = None
current = "O"

def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])

def handle_turn(player):
    print(player + "'s turn" )
    pos = int(input("Choose 1 - 9: ")) - 1
    while pos not in list(range(9)):
        pos = int(input("Incorrect input. Try again: ")) - 1
    while board[pos] != "-":
        pos = int(input("You can't go there. Try again: ")) - 1
    board[pos] = player
    display_board()

def check_rows():
    global gameOn
    global winner
    row1 = board[0] == board[1] == board[2] != "-"
    row2 = board[3] == board[4] == board[5] != "-"
    row3 = board[6] == board[7] == board[8] != "-"

    if row1 or row2 or row3:
        gameOn = False

    if row1:
        winner = board[0]

    elif row2:
        winner = board[3]

    elif row3:
        winner = board[6]

    else:
        winner = None
    return winner

def check_columns():
    global gameOn
    global winner
    col1 = board[0] == board[3] == board[6] != "-"
    col2 = board[1] == board[4] == board[7] != "-"
    col3 = board[2] == board[5] == board[8] != "-"

    if col1 or col2 or col3:
        gameOn = False

    if col1:
        winner = board[0]

    elif col2:
        winner = board[1]

    elif col3:
        winner = board[2]

    else:
        winner = None
    return winner

def check_diagonals():
    global gameOn
    global winner
    diag1 = board[0] == board[4] == board[8] != "-"
    diag2 = board[2] == board[4] == board[6] != "-"

    if diag1 or diag2:
        gameOn = False

    if diag1:
        winner = board[0]

    elif diag2:
        winner = board[2]

    else:
        winner = None
    return winner

def win():
    global winner
    row_winner = check_rows()
    column_winner = check_columns()
    diagonal_winner = check_diagonals()

    if row_winner:
        winner = row_winner
        return winner
    elif column_winner:
        winner = column_winner
        return winner
    elif diagonal_winner:
        winner = diagonal_winner1
        return winner

def tie():
    global gameOn
    if "-" not in board:
        gameOn = False
    return

def gameOver():
    win()
    tie()

def flip():
    global current
    if current == "O":
        current = "X"

    elif current == "X":
        current = "O"
    return current


def play_game():
    display_board()
    while gameOn:
        handle_turn(current)
        gameOver()
        flip()

    if winner == "X" or winner == "O":
        print("Winner is " + winner)
    elif winner == None:
        print("Tie.")

play_game()
