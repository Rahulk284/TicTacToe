# board
gamerun = True
board = ['-', '-', '-', '-', '-', '-', '-', '-', '-']
player1 = input('Who is X: ')
player2 = input('Who is O: ')
turns = [0, 1, 2, 3, 4, 5, 6, 7, 8]
usedspot = [0, 1, 2, 3, 4, 5, 6, 7, 8]
n = 1

# displayboard
def displayboard():
    print(board[0] + '|' + board[1] + '|' + board[2])
    print(board[3] + '|' + board[4] + '|' + board[5])
    print(board[6] + '|' + board[7] + '|' + board[8])

# play game
def playgame():
    global gamerun
    while gamerun == True:
        playerturn()
        checkcolumn()
        checkrow()
        checkdiagonal()
        checkwin()
        checktie()

def playerturn():
    global n
    if n % 2 != 0:
        displayboard()
        turnchoice = boardplace(player1)
        board[turnchoice] = 'X'
    else:
        displayboard()
        turnchoice = boardplace(player2)
        board[turnchoice] = 'O'
    n += 1

def boardplace(player):
    turnchoice = int(input(player + ' pick a place on the board from 1-9: '))
    turnchoice = turnchoice - 1
    while turnchoice not in turns:
        turnchoice = int(input(player + ' pick a place on the board from 1-9: '))
        turnchoice = turnchoice - 1
    while turnchoice not in usedspot:
        turnchoice = int(input('Place already used please pick another: '))
        turnchoice = turnchoice - 1 
        while turnchoice not in turns:
            turnchoice = int(input(player + ' pick a place on the board from 1-9: '))
            turnchoice = turnchoice - 1
    usedspot.remove(turnchoice)
    return turnchoice

def checkrow():
    global gamerun
    row1 = board[0] == board[1] == board[2] != '-'
    row2 = board[3] == board[4] == board[5] != '-'
    row3 = board[6] == board[7] == board[8] != '-'
    if row1 or row2 or row3:
        gamerun = False

    if row1:
        return board[0]
    elif row2:
        return board[3]
    elif row3:
        return board[6]

def checkcolumn():
    global gamerun
    column1 = board[0] == board[3] == board[6] != '-'
    column2 = board[1] == board[4] == board[7] != '-'
    column3 = board[2] == board[5] == board[8] != '-'
    if column1 or column2 or column3:
        gamerun = False

    if column1:
        return board[0]
    elif column2:
        return board[1]
    elif column3:
        return board[2]

def checkdiagonal():
    global gamerun
    diagonal1 = board[0] == board[4] == board[8] != '-'
    diagonal2 = board[2] == board[4] == board[6] != '-'
    if diagonal1 or diagonal2:
        gamerun = False

    if diagonal1:
        return board[0]
    elif diagonal2:
        return board[2]

def checkwin():
    if checkcolumn() == 'X':
        displayboard()
        print(player1 + ' Wins!')
    elif checkcolumn == 'O':
        displayboard()
        print(player2 + ' Wins!')
    elif checkrow() == 'X':
        displayboard()
        print(player1 + ' Wins!')
    elif checkrow == 'O':
        displayboard()
        print(player2 + ' Wins!')
    elif checkdiagonal() == 'X':
        displayboard()
        print(player1 + ' Wins!')
    elif checkdiagonal == 'O':
        displayboard()
        print(player2 + ' Wins!')

def checktie():
    global gamerun
    if '-' not in board:
        displayboard()
        print('Tie!')
        gamerun = False

playgame()
