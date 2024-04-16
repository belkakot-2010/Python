import tkinter

'''
Вопрос: Label
Ответы: Button
Счёт: кол-во прввильных ответов
'''

'''
текст вопрса
варианты ответов
правильный ответ
'''

question = [
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
    }
]


class App:
    '''Приложение'''
    def __init__(self, width: int, height: int) -> None:
        self.window = tkinter.Tk()
        self.window.option_add('*Font', ('Consolas', 30))
        self.wight = width
        self.height = height
        self.window.geometry(f'{self.wight}x{self.height}')
        self.question_num = None
        self.label_question_text = None
        self.label_answer_text_1 = None
        self.label_answer_text_2 = None
        self.label_answer_text_3 = None
        self.label_answer_text_4 = None
        self.button_answer_1 = None
        self.button_answer_2 = None
        self.button_answer_3 = None
        self.button_answer_4 = None
        self.make_widgets
        self.position_widgets()
        self.start()
        self.window.mainloop()


    def make_widgets(self) -> None:
        '''Создают экземпляры виджетов'''
        self.label_question_text = tkinter.label(self.window)
        self.label_answer_text_1 = tkinter.label(self.window)
        self.label_answer_text_2 = tkinter.label(self.window)
        self.label_answer_text_3 = tkinter.label(self.window)
        self.label_answer_text_4 = tkinter.label(self.window)
        self.button_answer_1 = tkinter.answer(self.window, text='1', command=self.on_clik(1))
        self.button_answer_2 = tkinter.answer(self.window, text='2', command=self.on_clik(2))
        self.button_answer_3 = tkinter.answer(self.window, text='3', command=self.on_clik(3))
        self.button_answer_4 = tkinter.answer(self.window, text='4', command=self.on_clik(4))

    def position_widgets(self) -> None:
        '''Позиционирует виджеты в окне'''
        self.label_question_text.pack() 
        self.label_answer_text_1.pack()
        self.label_answer_text_2.pack()
        self.label_answer_text_3.pack()
        self.label_answer_text_4.pack()
        self.button_answer_1.pack()
        self.button_answer_2.pack()
        self.button_answer_3.pack()
        self.button_answer_4.pack()

    def start(self) -> None:
        self.question_num = 0
        self.label_question_text['text'] = question[self.question_num]['Текст вопроса']
        self.label_answer_text_1['text'] = '1.' + question[self.question_num]['Варианты ответов'][0]
        self.label_answer_text_2['text'] = '2.' + question[self.question_num]['Варианты ответов'][1]
        self.label_answer_text_3['text'] = '3.' + question[self.question_num]['Варианты ответов'][2]
        self.label_answer_text_4['text'] = '4.' + question[self.question_num]['Варианты ответов'][3]

    def on_clik(self, button_num) -> None:
        print('Нажата кнопка', button_num)


App()