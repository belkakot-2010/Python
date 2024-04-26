import tkinter as tk
import random


questions = [
    {
        'Текст вопроса': 'Чей Крым?',
        'Варианты ответов': ['Россия', 'Украина', 'Турция', 'Третий Рейх'],
        'индекс верного ответа': 'Россия'
    },
    {
        'Текст вопроса': 'Столица РФ?',
        'Варианты ответов': ['Киев', 'Санкт-Петербург', 'Москва', 'Мухосранск'],
        'индекс верного ответа': 'Москва'
    },
    {
        'Текст вопроса': 'Cколько морей омывает РФ?',
        'Варианты ответов': ['0', '7', '13', '12'],
        'индекс верного ответа': '12'
    },
    {
        'Текст вопроса': 'Самая высокая гора России?',
        'Варианты ответов': ['Эльбрус', 'Белуха', 'Ключевская сопка', 'Кудыкина гора'],
        'индекс верного ответа': 'Белуха'
    },
    {
        'Текст вопроса': 'Самая длинная река России?',
        'Варианты ответов': ['Волга', 'Москва', 'Лена', 'Колыма'],
        'индекс верного ответа': 'Лена'
    },
    {
        'Текст вопроса': 'Какой из этих городов самый старый?',
        'Варианты ответов': ['Москва', 'Королёв', 'Великий Новгород', 'Дербент'],
        'индекс верного ответа': 'Дербент'
    },
    {
        'Текст вопроса': 'На какой реке находится Санкт-Петербург?',
        'Варианты ответов': ['Нева', 'Москва', 'Анадырь', 'Кубань'],
        'индекс верного ответа': 'Нева'
    },
    {
        'Текст вопроса': 'Самая северная точка России?',
        'Варианты ответов': ['Арбат', 'Мыс Дежнёва', 'Мыс Челюскин', 'Крым'],
        'индекс верного ответа': 'Мыс Челюскин'
    },
    {
        'Текст вопроса': 'Какой город был столицей России?',
        'Варианты ответов': ['Ростов', 'Владимир', 'Нижний Новгород', 'Не один из перечисленных'],
        'индекс верного ответа': 'Владимир'
    },
    {
        'Текст вопроса': 'Первый правитель России?',
        'Варианты ответов': ['Рюрик', 'Пётр 1', 'Путин', 'Иван Грозный'],
        'индекс верного ответа': 'Рюрик'
    },
]


class App:
    def __init__(self, shuffle_question=False) -> None:
        self.window = tk.Tk()
        self.window.bind('<Escape>', lambda _: self.window.destroy)
        self.window.option_add('*Font', ('Consolas', 30))

        self.width = self.window.winfo_screenwidth()
        self.height = self.window.winfo_screenheight()
        self.window.geometry(f'{self.width}x{self.height}')

        self.main_frame = tk.Frame(self.window)
        self.main_frame.place(relx=0.5, rely=0.5, anchor='center')

        self.question_index = None
        self.correct_answers = None
        self.incorrect_answers = None
        self.shuffle_question = None

        self.start()
        self.window.mainloop()


    def start(self) -> None:
        self.question_index = 0
        self.correct_answers = 0
        self.incorrect_answers = 0 
        if self.shuffle_question:
            random.shuffle(questions)
        self.show_question()

    def show_question(self) -> None:
        question = question[self.question_index]
        tk.Label(self.main_frame, text=question['Текст вопроса']).pack()
        for answer in question['Варианты ответов']:
            tk.Button(self.main_frame, text=answer, command= lambda arg=answer: self.on_button(arg)).pack

    def on_button(self, button_text) -> None:
        question = question[self.question_index]
        if button_text == question['индекс верного ответа']:
            self.correct_answers += 1
        else:
            self.incorrect_answers += 1

        for widget in self.main_frame.winfo_children():
            widget.destroy()

        self.question_index += 1
        if self.question_index < len(question):
            self.show_question()
        else:
            self.show_result

    def show_result(self) -> None:
        tk.Label(self.main_frame, text=f'верно: {self.correct_answers}').pack
        tk.Label(self.main_frame, text=f'неверно: {self.incorrect_answers}').pack
        tk.Button(self.main_frame, text='заново' command=self.start()).pack




App(shuffle_question=True)