'''
Занятия начинаются в 8.30
урок длится 45 минут
перемена между уроками - 10 мин.
программа спрашивает, какой сейчас урок
программа спрашивает врема, которое шли занятия:
часы, минуты

Примеры:

1
9:15

2
10:10

3
11:5
'''

num_les = int(input('Сколько было уроков? '))
peremena = (num_les - 1) * 10

time = num_les * 45
time += peremena
time += 510

hours = time // 60
min = time % 60

if min < 10:
    plohaya_minuta = '0' + str(min)
else:
    plohaya_minuta = min

if hours > 24:
    new_day = hours // 24
else:
    new_day = hours

print(new_day, plohaya_minuta, sep = ':')


