# -*-coding:utf-8-*-
import game


# 输出菜单
def menu():
    print("*******************************")
    print("*****    1.play 0.exit    *****")
    print("*******************************")


# 游戏开始
def game_start():
    # 初始化棋盘
    board = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']
    ]
    game.display_board(board)
    # 游戏开始
    while True:
        # 玩家走
        game.player_move(board)
        game.display_board(board)
        ret = game.is_win(board)
        if ret != 'Continue':
            break
        # 电脑走
        game.computer_move(board)
        game.display_board(board)
        ret = game.is_win(board)
        if ret != 'Continue':
            break
    # 判断输赢
    if ret == '*':
        print("玩家赢")
    elif ret == '#':
        print("电脑赢")
    else:
        print("平局")


def test():
    while True:
        menu()
        option = int(input("请选择:>"))
        if option == 1:
            print("井字棋")
            game_start()
            break
        elif option == 0:
            print("退出游戏")
            break
        else:
            print("输入错误，请重新输入")
            break


if __name__ == '__main__':
    test()
