import random

board = [' '] * 10
computer = 'X'
human = 'O'

def display_board(board):
    print(f'{board[1]} | {board[2]}  | {board[3]}')
    print(f'{board[4]} | {board[5]}  | {board[6]}')
    print(f'{board[7]} | {board[8]}  | {board[9]}')
    print("_" * 10)

def check_win():
    winning_combinations = [
        (1, 2, 3),
        (4, 5, 6),
        (7, 8, 9),
        (1, 4, 7),
        (2, 5, 8),
        (3, 6, 9),
        (1, 5, 9),
        (3, 5, 7)
    ]

    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != ' ':
            return True

    return False

def check_draw():
    return ' ' not in board[1:]

def is_available(pos):
    return board[pos] == ' '

def insert(letter, pos):
    if is_available(pos):
        board[pos] = letter
        display_board(board)
        if check_win():
            if letter == 'X':
                print("Computer wins!")
            else:
                print("Human wins!")
            return True  
        if check_draw():
            print("It's a draw!")
            return True  
    else:
        if letter == 'O':
            print("Position not free, re-enter a position")
            human_move(letter)
        else:
            computer_move(letter)
    return False  

def human_move(letter):
    pos = int(input("Enter the position to insert (1-9): "))
    insert(letter, pos)

def computer_move(letter):
    pos = random.randint(1, 9)
    while not is_available(pos):
        pos = random.randint(1, 9)
    insert(letter, pos)

def play_game():
    print("Welcome to Tic Tac Toe!")
    display_board(board)
    while not check_win() and not check_draw():
        human_move(human)
        if check_win() or check_draw():
            break
        computer_move(computer)

play_game()
