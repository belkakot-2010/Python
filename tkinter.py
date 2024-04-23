import tkinter


questions = [
    {
        'Текст вопроса': 'Чей Крым?',
        'Варианты ответов': ['Россия', 'Украина', 'Турция', 'Третий Рейх'],
        'индекс верного ответа': 0
    },
    {
        'Текст вопроса': 'Столица РФ?',
        'Варианты ответов': ['Киев', 'Санкт-Петербург', 'Москва', 'Мухосранск'],
        'индекс верного ответа': 2
    },
    {
        'Текст вопроса': 'Cколько морей омывает РФ?',
        'Варианты ответов': ['0', '7', '13', '12'],
        'индекс верного ответа': 3
    },
    {
        'Текст вопроса': 'Самая высокая гора России?',
        'Варианты ответов': ['Эльбрус', 'Белуха', 'Ключевская сопка', 'Кудыкина гора'],
        'индекс верного ответа': 1
    },
    {
        'Текст вопроса': 'Самая длинная река России?',
        'Варианты ответов': ['Волга', 'Москва', 'Лена', 'Колыма'],
        'индекс верного ответа': 2
    },
    {
        'Текст вопроса': 'Какой из этих городов самый старый?',
        'Варианты ответов': ['Москва', 'Королёв', 'Великий Новгород', 'Дербент'],
        'индекс верного ответа': 3
    },
    {
        'Текст вопроса': 'На какой реке находится Санкт-Петербург?',
        'Варианты ответов': ['Нева', 'Москва', 'Анадырь', 'Кубань'],
        'индекс верного ответа': 0
    },
    {
        'Текст вопроса': 'Самая северная точка России?',
        'Варианты ответов': ['Арбат', 'Мыс Дежнёва', 'Мыс Челюскин', 'Крым'],
        'индекс верного ответа': 2
    },
    {
        'Текст вопроса': 'Какой город был столицей России?',
        'Варианты ответов': ['Ростов', 'Владимир', 'Нижний Новгород', 'Не один из перечисленных'],
        'индекс верного ответа': 1
    },
    {
        'Текст вопроса': 'Первый правитель России?',
        'Варианты ответов': ['Рюрик', 'Пётр 1', 'Путин', 'Иван Грозный'],
        'индекс верного ответа': 0
    },
]


class App:
    '''Приложение'''
    def __init__(self) -> None:
        self.window = tkinter.Tk()
        self.window.option_add('*Font', ('Consolas', 30))
        self.width = self.window.winfo_screenwidth()
        self.height = self.window.winfo_screenheight()
        self.window.geometry(f'{self.width}x{self.height}')
        self.question_number = None
        self.label_question_text = None
        self.label_answer_text_1 = None
        self.label_answer_text_2 = None
        self.label_answer_text_3 = None
        self.label_answer_text_4 = None
        self.button_answer_1 = None
        self.button_answer_2 = None
        self.button_answer_3 = None
        self.button_answer_4 = None
        self.result_frame = None
        self.make_widgets()
        self.positon_widgets()
        self.start()
        self.window.mainloop()

    def make_widgets(self) -> None:
        '''Создает экземпляры виджетов'''
        self.question_frame = tkinter.Frame(self.window)
        self.label_question_text = tkinter.Label(self.question_frame)
        self.answers_frame = tkinter.Frame(self.question_frame)
        self.label_answer_text_1 = tkinter.Label(self.answers_frame)
        self.label_answer_text_2 = tkinter.Label(self.answers_frame)
        self.label_answer_text_3 = tkinter.Label(self.answers_frame)
        self.label_answer_text_4 = tkinter.Label(self.answers_frame)
        self.buttons_frame = tkinter.Frame(self.question_frame)
        self.button_answer_1 = tkinter.Button(
            self.buttons_frame, text='1', command=lambda: self.on_click(0)
        )
        self.button_answer_2 = tkinter.Button(
            self.buttons_frame, text='2', command=lambda: self.on_click(1)
        )
        self.button_answer_3 = tkinter.Button(
            self.buttons_frame, text='3', command=lambda: self.on_click(2)
        )
        self.button_answer_4 = tkinter.Button(
            self.buttons_frame, text='4', command=lambda: self.on_click(3)
        )

    def positon_widgets(self) -> None:
        '''Позиционирует виджеты в окне'''
        self.question_frame.pack(expand=True)
        self.label_question_text.pack(pady=35)
        self.answers_frame.pack(pady=35)
        self.label_answer_text_1.pack(anchor='w')
        self.label_answer_text_2.pack(anchor='w')
        self.label_answer_text_3.pack(anchor='w')
        self.label_answer_text_4.pack(anchor='w')
        self.buttons_frame.pack()
        self.button_answer_1.pack(side='left', padx=25)
        self.button_answer_2.pack(side='left', padx=25)
        self.button_answer_3.pack(side='left', padx=25)
        self.button_answer_4.pack(side='left', padx=25)

    def show_question(self) -> None:
        '''Показывает контент вопроса на экране'''
        question = questions[self.question_number]
        self.label_question_text['text'] = question['текст вопроса']
        self.label_answer_text_1['text'] = '1. ' + question['варианты ответов'][0]
        self.label_answer_text_2['text'] = '2. ' + question['варианты ответов'][1]
        self.label_answer_text_3['text'] = '3. ' + question['варианты ответов'][2]
        self.label_answer_text_4['text'] = '4. ' + question['варианты ответов'][3]

    def on_click(self, button_index: int) -> None:
        question = questions[self.question_number]
        if button_index == question['индекс верного ответа']:
            self.correct_answers += 1
        else:
            self.incorrect_answers += 1
        self.question_number += 1
        # Закончить викторину
        if len(questions) == self.question_number:
            self.show_result()
        else:
            self.show_question()

    def show_result(self) -> None:
        '''Показывает на экране результат викторины'''
        self.question_frame.pack_forget()
        self.result_frame = tkinter.Frame(self.window)
        self.result_frame.pack()
        tkinter.Label(self.result_frame, text='Викторина завершена!').pack()
        tkinter.Label(self.result_frame, text=f'Всего вопросов: {len(questions)}').pack()
        tkinter.Label(self.result_frame, text=f'Правильных ответов: {self.correct_answers}').pack()
        tkinter.Label(self.result_frame, text=f'Ошибок: {self.incorrect_answers}').pack()
        tkinter.Button(self.result_frame, text='начать заново', command=self.start).pack()

    def start(self) -> None:
        '''Начинает викторину заново'''
        self.question_number = 0
        self.correct_answers = 0
        self.incorrect_answers = 0
        if self.result_frame:
            self.result_frame.pack_forget()
        self.question_frame.pack()
        self.show_question()


App()
