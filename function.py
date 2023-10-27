def multiply(num_1, num_2):
    ''' Перемножает num_1 и num_2 и выводит произведение '''
    produkt = num_1 * num_2
    print(produkt)


def divide(num_1, num_2):
    ''' Разделяет num_1 и num_2 и выводит часное '''
    if num_2 == 0:
        print('ошибка')
    else:
        private = num_1 / num_2
        print(private)


def adition(num_1, num_2):
    ''' Складывает num_1 и num_2 и выводит сумму '''
    summ = num_1 + num_2
    print(summ)


def subtraction(num_1, num_2):
    ''' Вычитает num_1 из num_2 и выводит разность '''
    difference = num_1 - num_2
    print(difference)


multiply(2, 3)
adition(3, 5)
divide(20, 10)
subtraction(20, 10)