from random import shuffle
from os import system

'''
Карта
{
    'цена': 10,
    'масть': 'пик',
    'название': '10'
}

Масти:
    черви, пики, бубны, крести

Колода:
    на каждую масть карты от 6 до туза = 36 карт

Игроки
    от 2 до ...

Перетасовать колоду

Каждому игроку даем по 2 карты

Можно смотреть только свои карты

Ход
    беру еще карту (сколько угодно, не больше, чем осталось в колоде)
    или закончить ход

Каждый игрок делает 1 ход за партию

Если сумма цен всех карт игрока > 21, то он проиграл

Если все игроки проиграли, то это ничья

Побдитель - тот, кто набрал самую большую сумму цен своих карт
'''


def get_deck() -> list[dict]:
    '''Возвращает колоду карт'''
    suits = ('черви', 'пики', 'бубны', 'крести')
    cards = {
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        '10': 10,
        'валет': 2,
        'дама': 3,
        'король': 4,
        'туз': 11
    }
    deck = []
    for suit in suits:
        for item in cards:
            card = {
                'цена': cards[item],
                'масть': suit,
                'название': item
            }
            deck.append(card)
    return deck


def get_players() -> list[dict]:
    '''Возвращает список игроков'''
    player_1 = {
        'имя': 'Вася',
        'карты': [],
        'человек': True,
        'сумма': 0
    }
    player_2 = {
        'имя': 'Комп',
        'карты': [],
        'человек': False,
        'сумма': 0
    }
    return [player_1, player_2]


def deal_cards(num: int) -> None:
    '''Раздает кажому игроку по 2 карты'''
    for player in players:
        for i in range(num):
            player['карты'].append(deck.pop())


def show_cards() -> None:
    for card in player['карты']:
        print(card['название'], card['масть'])


def calculate_total_values(player: dict) -> None:
    total = 0
    for card in player['карты']:
        total += card['цена']
    player['сумма'] = total


def show_statistics() -> None:
    '''Выводит на экран очки игроков'''
    for player in players:
        if player['сумма'] > 21:
            print(player['имя'], player['сумма'], '- перебор!')
        else:
            print(player['имя'], player['сумма'])


deck = get_deck()
shuffle(deck)
players = get_players()
cards_per_turn = len(deck) // len(players)
deal_cards(2)

for player in players:
    while True:
        system('cls')
        show_cards()
        calculate_total_values(player)
        print('сумма очков:', player['сумма'])

        if player['человек']:
            player_option = input('Взять карту из колоды (y/n)? ')
        else:
            if player['сумма'] < 17:
                player_option = 'y'
            else:
                player_option = 'n'
        if player_option.lower() == 'y':
            if len(player['карты']) < cards_per_turn:
                player['карты'].append(deck.pop())
            else:
                print('Невозможно взять еще карту!')
                break
        else:
            break
    input('ENTER - следующий игрок')

system('cls')
show_statistics()


total_values = [player['сумма'] for player in players]


if total_values.count(total_values[0]) == len(total_values):
    print('Ничья')
else:
    total_values = [player['сумма'] for player in players if player['сумма'] < 21]

    for player in players:
        if player['сумма'] == max(total_values):
            if 
                print('Победил', ['имя'])