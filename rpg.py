import tkinter as tk
from classes import Weapons, Player
from PIL import Image, ImageTk
from pathlib import Path


class Game:
    def __init__(self) -> None:
        self.window = tk.Tk()
        self.window.attributes('-fullscren', True)
        self.window.bind('<Escape>', lambda event: self.window.destroy())
        self.player = Player('Пчел', 100, Weapons('нож', 1))
        self.enemy = Player('Гад', 100, Weapons('нож', 1))
        self.img_dir = Path(__file__).parent / 'img'
        self.make_hero_screen()
        self.window.mainloop()

    def make_hero_screen(self) -> None:
        frame = tk.Frame(self.window)
        frame.pack()
        image = Image.open(self.img_dir / self.player.img)
        image_wigth = self.window.winfo_screenwidth() // 3
        aspect_ratio = image.height / image.width
        image_height = int(image_wigth) * aspect_ratio
        image = image.resize((image_wigth, image_height))
        self.image_tk = ImageTk.PhotoImage(image=image)

        tk.Label(image=self.image_tk).pack()
        tk.Label(frame, text=self.player.name).pack()
        tk.Label(frame, text=f'здоровье: {self.player.hp}').pack()
        tk.Label(frame, text=self.player.weapon).pack()
        tk.Label(frame, text=f'сила: {self.player.power}').pack()
        tk.Label(frame, text=f'уровень: {self.player.lvl}').pack()
        tk.Label(frame, text=f'опыт: {self.player.xp}').pack()

    def make_enemy_screen(self) -> None:
        frame = tk.Frame(self.window)
        frame.pack()
        image = Image.open(self.img_dir / self.player.img)
        image_wigth = self.window.winfo_screenwidth() // 3
        aspect_ratio = image.height / image.width
        image_height = int(image_wigth) * aspect_ratio
        image = image.resize((image_wigth, image_height))
        self.image_tk = ImageTk.PhotoImage(image=image)

        tk.Label(image=self.image_tk).pack()
        tk.Label(frame, text=self.enemy.name).pack()
        tk.Label(frame, text=f'здоровье: {self.enemy.hp}').pack()
        tk.Label(frame, text=self.enemy.weapon).pack()
        tk.Label(frame, text=f'сила: {self.enemy.power}').pack()
        tk.Label(frame, text=f'уровень: {self.enemy.lvl}').pack()
        tk.Label(frame, text=f'опыт: {self.enemy.xp}').pack()


Game()
