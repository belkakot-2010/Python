'''
Игрово е поле из 9 клеток
игрок_1 - х
игрок_2 - 0
Игроки ходят по очереди
начинает х
Для победы необходимо разместить три одинаковых знака в ряд:
По горизонтали, по вертикале или по диагонали.
Ничья - нет возможности создать выигрышную комбинацию.
'''

from os import system
from random import choice


BatleField = ['.'] * 9


def draw_field(Batlefield: list) -> str:
    system('cls')
    for i in range(0, 7, 3):
        print(Batlefield[i], Batlefield[i + 1], Batlefield[i + 2])


def make_move_human(BatleField: list, player: str) -> None:
    while True:
        cell_num = int(input('Выберете клетку в которую сделаете ход '))
        if cell_num < 1 or cell_num > 9:
            print('Ошибка! Номер должен быть от 1 до 9')
            continue
        if BatleField[cell_num - 1] in players:
            print('Ошибка! Клетка занята')
            continue
        BatleField[cell_num - 1] = player
        break


def make_move_comp(BatleField: list, player: str, is_center: bool) -> None:
    cells_index = []
    for i in range(9):
        if BatleField[i] == '.':
            cells_index.append(i)
        if is_center and 4 in cells_index:
            BatleField[4] = player
        else:
            random_index = choice(cells_index)
            BatleField[random_index] = player



def get_winner(BatleField: list, player: str) -> str:
    for i in range(0, 7, 3):
        if BatleField[i] == BatleField[i + 1] == BatleField[i + 2] == player:
            return player        

    for i in range(0, 3, 1):
        if BatleField[i] == BatleField[i + 3] == BatleField[i + 6] == player:
            return player

    if BatleField[0] == BatleField[4] == BatleField[8] == player:
        return player
    
    if BatleField[2] == BatleField[4] == BatleField[6] == player:
        return player

    return ''


player_1 = 'x'
player_2 = '0'
players = (player_1, player_2)
moves = 1

while True:
    if moves > 9:
        draw_field(BatleField)
        print('Ничья')
        break
    draw_field(BatleField)
    if moves % 2:
        player = player_1
        make_move_human(BatleField, player)
    else:
        player = player_2
        make_move_comp(BatleField, player)
        
    moves += 1    
    winner = get_winner(BatleField, player)
    if winner: 
        draw_field(BatleField)
        print('Победил', winner)
        break


print('Игра окончена')