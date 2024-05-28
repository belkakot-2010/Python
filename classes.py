
class Weapons:
    '''Оружие'''
    def __init__(self, name: str, attac: int) -> None:
        self.name = name
        self.attac = attac

    def __str__(self) -> str:
        return f'{self.name}, ({self.attac})'

  
class Player:  # определяем класс
    '''Игрок'''
    def __init__(self, name: str, hp: int, weapon=None, lvl=1, xp=0, img = 'player_png') -> None:
        '''
        Конструктор класса
        Вызывается автоматически после создания экземпляра
        self - ссылка на экземпляр
        Все атрибуты определяютсяя в конструкторе
        '''
        self.name = name  # атрибут
        self.hp = hp
        self.weapon_default = Weapons('Кулаки', 1)
        if weapon:
            self.weapon = weapon
        else:
            self.weapon = self.weapon_default
        self.power = self.weapon.attac
        self.lvl = 1
        self.xp = 0
        self.image = 'player_png'

    def __str__(self) -> str:
        '''Этот метод автоматически вызывается при обращении к объекту как к строке'''
        return f'Игрок {self.name}, жизни: {self.hp}, оружие: {self.weapon}'

    def attack(self, enemy) -> None:
        # ход игрока (игрок атакует противника)
        if self.hp <= 0:
            return
        damage = self.power * self.weapon.attac
        enemy.hp -= damage
        print(self.name, 'атаковал', enemy.name)


class Enemy:  # определяем класс
    def __init__(self, enemy_name: str, enemy_hp: int, enemy_weapon=None, enemy_lvl=1, enemy_xp=0, enemy_img = 'enemy_png') -> None:
        self.enemy_name = enemy_name
        self.enemy_hp = enemy_hp
        self.enemy_weapon_default = Weapons('Кулаки', 1)
        if enemy_weapon:
            self.weapon = enemy_weapon
        else:
            self.enemy_weapon = self.enemy_weapon_default
        self.enemy_power = self.weapon.attac
        self.enemy_lvl = 1
        self.enemy_xp = 0
        self.enemy_image = 'enemy_png'

    
class Game:
    '''Игра'''
    def __init__(self) -> None:
        self.player = Player('Челик', 100, Weapons('Меч кладенец', 5))
        self.enemy = Player('Дурик', 100,)
        self.is_fighting = False
        # self.fight()
        
    def fight(self) -> None:
        '''Бой - обмен ударами'''
        self.is_fighting = True
        while self.is_fighting: 
            self.player.attack(self.enemy)
            print(self.player)
            self.enemy.attack(self.player)
            print(self.enemy)
            self.check_winner()
        print('Бой окончен')

            
    def check_winner(self) -> None:
        if self.player.hp <= 0:
            print(self.enemy.name, 'Победил')
            self.is_fighting = False
        elif self.enemy.hp <= 0:
            print(self.player.name, 'Победил')
            self.is_fighting = False


Game()
