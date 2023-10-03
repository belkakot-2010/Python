name = input('Как зовут твоего персонажа? ')

way_1 = False
way_2 = False
way_3 = False

while way_1 == False or way_2 == False or way_3 == False:

    print(name, 'Приехал к камню, а на нём надпись:')
    print('Налево поедешь - убит будешь')
    print('Прямо поедешь - богатым станешь')
    print('Направо поедешь - женатым станешь')

    way = input('В какую сторону ехать? ')    

    if way == 'налево':
        if way_1 == False:
            print(name, 'Попал на дорогу разбойников')
            choice = input('Что делать сражаться или уехать? ')         
            if choice == 'сражаться':
                print(name, 'Победил разбойников')
                way_1 = True
            else:
                print('Нужно зачастить дорогу - возвращайся')
                continue
        else:
           print(name, 'Уже был сдесь едь в другое место')
           
    elif way == 'прямо':
        if way_2 == False:
            print(name, 'Нащёл богатства')
            choice_2 = input('Что делать забрать или уехать? ')         
            if choice_2 == 'уехать':
                print(name, 'Понял, что на этой дороге делать нечего')
                way_2 = True
            else:
                print(name,'Попал в засаду разбойников и погиб, - возвращайся')
                continue
        else:
           print(name, 'Уже был сдесь едь в другое место')

    elif way == 'направо':
        if way_3 == False:
            print(name, 'Попал в терем к княжне')
            choice_3 = input('Княжна предлагает жениться на ней что сделаешь? ')         
            if choice_3 == 'убить':
                print(name, 'Убил княжну и освободил запертых молодцов')
                way_3 = True
            else:
                print(name,'Согласился и был заточён в темницу, - возвращайся')
                continue
        else:
            print(name, 'Уже был сдесь едь в другое место')

    else:
        print('Нет такой дороги')
        
print(name, 'Проехал все дороги, вот и сказке конец!')

    
    
