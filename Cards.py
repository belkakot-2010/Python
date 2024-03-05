from random import shuffle
from os import system


def get_deck() -> list[dict]:
    suits = ['Пики', 'Черви', 'Крести', 'Бубны']
    cards = {
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'В': 2,
    'Д': 3,
    'К': 4,
    'Т': 11
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
    player_1 = {
        'имя': 'Дурик',
        'Карты': [],
        'Человек': True,
        'Сумма': 0
    }

    player_2 = {
        'имя': 'Дебик',
        'Карты': [],
        'Человек': True,
        'Сумма': 0
    }
    return [player_1, player_2]


def deal_cards(num: int) -> None:
    for player in players:
        for i in range(num):
            player['Карты'].append(deck.pop())


def show_cards() -> None:
    for card in player['Карты']:
        print(card['название'], card['масть'])


deck = get_deck()     
shuffle(deck)
players = get_players()
deal_cards(2)


for player in players:
    while True:
        system('cls')
        show_cards()
        player_option = input('Взять карту из колоды? y/n ')
        if player_option.lower() == 'y':
            player['Карты'].append(deck.pop())
        else:
            break


system('cls')
for player in players:
    for card in players[0]['Карты']:
       player['Сумма'] += card['цена']
    print(player['имя'], player['Сумма'])


def get_winner(player):
    if player['Сумма'] > 21:
        print(player['имя'], 'Перебор')
    else:
        