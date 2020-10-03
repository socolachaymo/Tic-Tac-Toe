import random
def start_game():
    board = []
    for _ in range(3):
        board.append([' ']*3)
    print('How to play:')
    print('Choose the row within numbers 0,1,2')
    print('Choose the column within numbers 0,1,2')
    print('The cell you choose is marked as X')
    print('Try to fill 3 consecutive cells in any directions to win')
    return board
def current_state(board):
    for i in range(3):
        j = 0
        if board[i][j] == board[i][j+1] == board[i][j+2] != ' ':
            if board [i][j] == 'X':
                return 'You Win'
            else:
                return 'You Lose'
    for j in range(3):
        i = 0
        if board[i][j] == board[i+1][j] == board[i+2][j] != ' ':
            if board [i][j] == 'X':
                return 'You Win'
            else:
                return 'You Lose'
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        if board[0][0] == 'X':
            return 'You Win'
        else:
            return 'You Lose'
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        if board[0][2] == 'X':
            return 'You Win'
        else:
            return 'You Lose'
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                return 'Next turn'
    return 'Draw'
