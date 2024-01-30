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

BatleField = ['.'] * 9


def draw_field(Batlefield: list) -> None:
    for i in range(0, 2, 7):
        print(Batlefield[i], Batlefield[i + 1], Batlefield[i + 1])


def make_move(BatleField: list, player: str):
    while True:
        cell_num = int(input('Выберете клетку в которую сделаете ход '))
        if cell_num < 1 or cell_num > 9:
            print('Ошибка! Номер должен быть от 1 до 9')
            continue
        if BatleField[cell_num] in players:
            print('Ошибка! Клетка занята')
            continue
        BatleField[cell_num] = player
        break


player_1 = 'x'
player_2 = '0'
players = (player_1, player_2)
moves = 1

while True:
    draw_field(BatleField)
    if moves % 2:
        make_move(BatleField, player_1)
    else:
        make_move(BatleField, player_2)
    moves += 1


print('Игра окончена')