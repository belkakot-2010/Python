from random import randint

player_name = input('Как зовут твоего бойца? ')
player_hp = 100
player_level = 1
player_xp = 10
money = 100

while True:
    print('1 - сражаться')
    print('2 - поехать в трактир')
    print('0 - уйти')
    print('3 - магазин')
    option = input('Введите номер ответа и нажмите энтер: ')

    if option == '1':
        enemy_name = 'Буйный плохиш'
        enemy_hp = 100
        enemy_level = 1
        enemy_xp = 10

        while player_hp > 0:
            damage = randint(0, 10)
            enemy_hp -= damage
            print(player_name, 'ударил', enemy_name,'на', damage, 'жизней')
            print('У', enemy_name, 'оcталось', enemy_hp, 'жизней' )
            if enemy_hp <= 0:
                print(player_name, 'Выиграл бой')
                player_xp += damage        
                if player_xp >= 10:
                    player_level += player_xp // 10
                    player_xp += enemy_xp % 10
                    money += player_level * 100
                    print('У', player_name, money, 'Монет')
                print(enemy_name, 'Погиб в бою')
                break        

            damage = randint(0, 10)
            player_hp -= damage
            print(enemy_name, 'ударил', player_name,'на', damage, 'жизней')
            print('У', player_name, 'оcталось', player_hp, 'жизней' )
            if player_hp <= 0:            
                print(player_name, 'Погиб в бою')              
                break    
                        
    elif option == '2':
        while True:
            enemy_name = 'Буйный посетитель'
            print(player_name, 'Приехал в таверну')
            print('1 - Сыграть в кости с посетителем в кости')
            print('0 - Уйти из таверны')
            option = input('Выбери свои действия ')
            if option == '1':
                if money <= 0:
                    print('У тебя не хватает денег!')
                    continue
                bet = int(input('Сколько поставишь? '))
                if bet <= 0:
                    print('Ставка не может быть меньше или равна нулю')
                    continue
                if bet > money:
                    print('Cтавка не может быть больше кол-ва денег')
                    continue
                player_score = randint(2, 12)
                enemy_score = randint(2, 12)
                print(player_name, 'Выбросил', player_score)
                print(enemy_name, 'Выбросил', enemy_score)
                if player_score > enemy_score:
                    money += bet
                    print(player_name, 'получил', bet, 'монет')
                elif player_score < enemy_score:
                    money -= bet
                    print(enemy_name, 'получил', bet, 'монет')
                else:
                    print('Ничья')

            elif option == '0':
                print(player_name, 'уехал из таверны')
                break
                        
            else:
                print('Нет такого варианта')

    elif option == '3':
        print(player_name, 'Прибыл в магазин')
        print('1 - оружие')
        print('2 - броня')
        print('3 - медикаменты')
        print('0 - уйти')
        option = int(input('Какой товар будете брать? '))        
        if option == 1:
        elif option == 2:
            
        elif option == 3:
            
        elif option == 0:
            print(player_name, 'Уехал из магазина')
        else:
            print('Нет такого варианта')
        
    elif option == '0':
        print(player_name, 'Уехал')
        break

    else:
        print('Ето не существующий путь')
  
print('Конец игры')
