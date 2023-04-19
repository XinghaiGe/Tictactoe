# -*-coding:utf-8-*-
import random


# 显示棋盘
def display_board(board):
    for i in range(0, 3):
        for j in range(0, 3):
            print(' ' + board[i][j] + ' ', end='')
            if j < 2:
                print('|', end='')
        print()
        if i < 2:
            for j in range(0, 3):
                print("---", end='')
                if j < 2:
                    print('|', end='')
            print()


# 玩家下棋
def player_move(board):
    print("玩家走")
    while True:
        print("请输入横坐标:>", end='')
        x = int(input())
        print("请输入纵坐标:>", end='')
        y = int(input())
        if (1 <= x <= 3) & (1 <= y <= 3):
            if board[x-1][y-1] == ' ':
                board[x - 1][y - 1] = '*'
                break
            else:
                print("该坐标被占用")
        else:
            print("坐标非法，请重新输入！")


# 电脑下棋
def computer_move(board):
    print("电脑走")
    while True:
        x = random.randint(0, 2)
        y = random.randint(0, 2)
        if board[x][y] == ' ':
            board[x][y] = '#'
            break


# 判断棋盘是否下满
def is_full(board) -> bool:
    for row in board:
        for col in row:
            if col == ' ':
                return False
    return True


# 判断输赢
def is_win(board) -> str:
    # 连成一行
    for i in range(0, 3):
        if board[i][0] == board[i][1] and board[i][1] == board[i][2] and board[i][1] != ' ':
            return board[i][1]
    # 连成一列
    for j in range(0, 3):
        if board[0][j] == board[1][j] and board[1][j] == board[2][j] and board[1][j] != ' ':
            return board[1][j]
    # 主对角线
    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[1][1] != ' ':
        return board[1][1]
    # 副对角线
    if board[2][0] == board[1][1] and board[1][1] == board[0][2] and board[0][2] != ' ':
        return board[1][1]
    if is_full(board):
        return 'Quit'
    return 'Continue'
