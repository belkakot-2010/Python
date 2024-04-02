'''
ООП - стиль програмирования
Класс - идея объекта
Экземпляр - конкретная реализация идеи
Переменные и функции внутри класс - атрибуты методы
'''


class Player:  # определяем класс
    '''Игрок'''
    def __init__(self, name: str, hp: int) -> None:
        '''
        Конструктор класса
        Вызывается автоматически после создания экземпляра
        self - ссылка на экземпляр
        Все атрибуты определяютсяя в конструкторе
        '''
        self.name = name  # атрибут
        self.hp = hp
        self.power = 1

    def __str__(self) -> str:
        return f'Игрок {self.name}, жизни: {self.hp}'
    

    def attack(self, enemy):
            enemy.hp -= self.power
            print(self.name, 'атаковал', enemy.name)


    
p1 = Player('Челик', 100)
p2 = Player('Дурик', 101)
print(p1)
print(p2)
    

class Game:
    def __init__(self) -> None:
        self.player = Player('Челик', 100)
        self.enemy = Player('Дурик', 100)
        self.fight()
        
    def fight(self) -> None:
        while True: 
            self.player.attack(self.enemy)
            print(self.player)
            self.enemy.attack(self.player)
            print(self.enemy)
      
        print('Бой окончен!')


Game()