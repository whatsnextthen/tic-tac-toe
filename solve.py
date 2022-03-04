# tic-tac-toe

board = []

for i in range(1, 10):
    board.append(str(i))

space = "  "

def print_board(board):
    print("-" * 25)
    for i in range(1, 10):
        print("|  ", board[i - 1], "  ", end = "")
        if (i % 3 == 0):
            print("|")
    print("-" * 25)

def check(value):
    if board[value - 1] != 'X' and board[value - 1] != 'O':
        return True
    else:
        return False

def check_if_win():
    win = 0
    for i in range(0, 9, 3):
        if board[i] == board[i + 1] and board[i] == board[i + 2] and board[i + 1] == board[i + 2]:
            win = 1
    for i in range(0, 3):
        if board[i] == board[i + 3] and board[i + 3] == board[i + 6] and board[i] == board[i + 6]:
            win = 1
    if board[0] == board[4] and board[4] == board[8] and board[0] == board[8]:
        win = 1
    if board[6] == board[4] and board[4] == board[2] and board[2] == board[6]:
        win = 1
    return win

def check_value(value):
    if not value.isdigit():
        return False
    if int(value) >= 1 and int(value) <= 9:
        return True
    else:
        return False

def check_S(S):
    if S == "X" or S == "O":
        return True
    else:
        return False

def request():
    print_board(board)
    print("Введите номер клетки в которую Вы хотите сыграть")
    OK = False
    while not OK:
        value = input()
        while not check_value(value):
            print("Неккоректный ввод. Введите ваш запрос еще раз")
            value = input()
        value = int(value)
        OK = check(value)
        if not OK:
            print("Данное поле уже занято. Введите координаты свободного поля")
    print("Введите что Вы хотите поставить в данную клетку")
    S = input()
    while not check_S(S):
        print("Неккоректный ввод. Введите ваш запрос еще раз")
        S = input()
    board[value - 1] = S
    return

print("Чтобы начать игру - нажмите любую клиавишу + Enter")

start = input()

win = 0

for K in range(9):
    request()
    if (check_if_win()):
        print_board(board)
        print("Поздравляем Вас, Вы победили!")
        win = 1
        break
if not win:
    print("Ничья!")
