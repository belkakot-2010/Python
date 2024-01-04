from random import choice


'''
Герой - список:
    1. Имя
    2. Здоровье
    3. Уровень
    4. Опыт
    5. Деньги
    6. Инвентарь
'''


def get_hero(name=None, hp=100, level=1, xp=0, money=100, inventory=None) -> list:
    '''Возвращает список характеристик героя'''
    if not name:
        names = ('Меченый', 'Артём', 'Артур', 'Хазбула', 'Чепух')
        name = choice(names)
    if not inventory:
        inventory = []
    return [name, hp, level, xp, money, inventory]


def show_hero(hero: list) -> None:
    '''Выводит на экран характеристики персонажа построчно'''
    print('Имя:', hero[0])
    print('Здоровье:', hero[1])
    print('Уровень:', hero[2])
    print('Опыт:', hero[3])
    print('Деньги:', hero[4])
    print('Инвентарь:', hero[5])


def show_enumerated_items(items: list) -> None:
     ''' Выводит на экран пронумерованные предметы '''
     for num, item in enumerate(items, 1):
            print(f'{num} - {item}')


def chek_option(items: list) -> str:
    ''' Создаёт и проверяет опцию на корректность и возвращает её '''
    print('0 - Выйти из режима покупки')
    option = input('Выберете номер товара ')
    if option == '0':
        print('Отмена покупки')
    elif int(option) < 0 or int(option) > len(shop_items):
        print('Нет такого товара')
        return ''
    else:
        return option


def visit_shop(hero: list, shop_items: list):
    '''
    Выводит на экран информацию о герое
    Выводит на экран текст магазина
    Выводит на экран опции
    Даёт возможность игроку выбрать опцию
    Действует по выбранной опции
    '''

    show_hero(hero)
    print(f'{hero[0]} приехал в лавку торговца. ')
    print('В лавке распродажа всё по 10!')
    price_tmp = 10
    print('1 - Купить товар')
    print('2 - Продать товар')
    print('0 - Выйти из лавки')
    option = input('Введите номер опции: ')

    if option == '1':
        show_enumerated_items(shop_items)
        option = chek_option(shop_items)
        if 
        if hero[4] < price_tmp:
            print('Не хватает денег')
        else:
            hero[4] -= price_tmp
            item_index = int(option) - 1
            item_name = shop_items[item_index]
            hero[5].append(item_name)
            shop_items.pop(item_index)
            print(shop_items)
            print(hero[5])


player = get_hero()
shop_items = ['Аптечка', 'Бинт', 'Консерва']
visit_shop(player, shop_items)
