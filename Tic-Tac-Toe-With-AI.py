import random,time
#board = ',X,O,,X,X,O,O,,O'.split(',')

def printboard(bo):
    print(f'{bo[7]} | {bo[8]} | {bo[9]}')
    print('----------')
    print(f'{bo[4]} | {bo[5]} | {bo[6]}')
    print('----------')
    print(f'{bo[1]} | {bo[2]} | {bo[3]}')
    return ("")

def chooseletter():
    choice = ' '
    while choice not in ('X','O'):
        print("Which letter do you want to be X or O")
        choice = input().upper()
    return ['X','O'] if choice == 'X' else ['O','X']

def who_goes_first():
    d = {0:'Computer',1:'Player'}
    turn = d[random.randint(0,1)]
    return turn

def move(bo,letter,pos):
    bo[pos] = letter

def movement_player():
    pos = " "
    while pos not in "1,2,3,4,5,6,7,8,9".split(',') or not free_space(board,int(pos)):
        print("Choose a position to move on!")
        pos = input()
    return int(pos)

def free_space(bo,pos):
    return bo[pos] == " "

def iswinner(bo,letter):
    if bo[1] == letter and bo[2] == letter and bo[3] == letter:
        return True
    if bo[4] == letter and bo[5] == letter and bo[6] == letter:
        return True
    if bo[7] == letter and bo[8] == letter and bo[9] == letter:
        return True
    if bo[1] == letter and bo[4] == letter and bo[7] == letter:
        return True
    if bo[2] == letter and bo[5] == letter and bo[8] == letter:
        return True
    if bo[3] == letter and bo[6] == letter and bo[9] == letter:
        return True
    if bo[1] == letter and bo[5] == letter and bo[9] == letter:
        return True
    if bo[3] == letter and bo[5] == letter and bo[7] == letter:
        return True
    return False

def boardfull(bo):
    if " " not in board[1:]:
        return True
    return False

def movement_computer(bo,player_letter,computer_letter):
    player = player_letter
    comp = computer_letter
    def copy_board(bo):
        return [i for i in bo]

    possible = [i for i in range(1,10) if free_space(copy_board(bo),i) == True]

    for x in possible:
        copy_bo = copy_board(bo)
        move(copy_bo,comp,x)
        if iswinner(copy_bo,comp):
            return x

    for x in possible:
        copy_bo = copy_board(bo)
        move(copy_bo,player,x)
        if iswinner(copy_bo,player):
            return x

    corners = [i for i in (1,3,7,9) if free_space(bo,i) == True]
    if corners != []:
        return random.choice(corners)

    if free_space(bo,5):
        return 5

    sides = [i for i in (2,4,6,8) if free_space(bo,i) == True]
    if sides != []:
        return random.choice(sides)

print("Welcome to tic-tac-toe!")
while True:
    board = ((', ')*9).split(',')
    print(printboard(board))
    player_letter,computer_letter = chooseletter()
    turn = who_goes_first()
    print(f'{turn} will go first')

    while True:
        if turn == 'Player':
            print(f"Player's Move,{player_letter}")
            position = movement_player()
            move(board,player_letter,position)
            if iswinner(board,player_letter):
                print(printboard(board))
                print("you have won!")
                break
            else:
                if boardfull(board):
                    print(printboard(board))
                    print("This game is a tie")
                    break
                else:
                    print(printboard(board))
                    turn = 'Computer'
        else:
            print("Computer's Move")
            time.sleep(1)
            comp_pos = movement_computer(board,player_letter,computer_letter)
            move(board,computer_letter,comp_pos)
            if iswinner(board,computer_letter):
                print(printboard(board))
                print("Computer has won!")
                break
            else:
                if boardfull(board):
                    print(printboard(board))
                    print("This game is a tie")
                    break
                else:
                    print(printboard(board))
                    turn = 'Player'
    repeat = input('Do you wish to play again(Y/N)?')
    if not repeat.lower().startswith('y'):
        break


