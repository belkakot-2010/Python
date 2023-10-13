from random import randint

player_name = input('Как зовут твоего бойца? ')
player_hp = 1050
player_level = 1
player_xp = 10
money = 0

while True:
    print('1 - сражаться')
    print('2 - играть в кости')
    print('0 - уйти')
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
            if player_hp <= 0:
                print(enemy_name, 'Выиграл бой')
                player_xp += enemy_xp        
                if player_xp >= 10:
                    player_level += player_xp // 10
                    player_xp += enemy_xp % 10   
                print(player_name, 'Погиб в бою')
                break        

            damage = randint(0, 10)
            player_hp -= damage
            print(enemy_name, 'ударил', player_name,'на', damage, 'жизней')
            print('У', player_name, 'оcталось', player_hp, 'жизней' )
            if enemy_hp <= 0:
                print(player_name, 'Выиграл бой')
                enemy_xp += player_xp
                if enemy_xp >= 10:
                    enemy_level += enemy_xp // 10
                    enemy_xp += player_xp % 10              
                print(enemy_name, 'Погиб в бою')
                prize == player_level * 100
                print(player_name, 'Получил', prize)
                break
        print(player_name, 'достиг', player_level, 'уровня')
        print(enemy_name, 'достиг', enemy_level, 'уровня')      
                        
    elif option == '2':
        if money >= 100:
            print('Играем')
            bet = int(input('Сколько поставишь? '))
            if bet >= money:
                print('Ставка принята')

                
            else:
                print('Нехватает денег, сбавь ставку')
        else:
            print('Денег нету')
        
    elif option == '0':
        print(player_name, 'Уехал')
        break
  

