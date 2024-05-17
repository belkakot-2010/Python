import tkinter as tk
import random
import datetime
import question
import os
from PIL import Image, ImageTk

questions = question.questions


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
        self.pady = 30

        self.question_index = None
        self.correct_answers = None
        self.incorrect_answers = None
        self.shuffle_question = None

        self.total_time = None
        self.start_time = None
        self.end_time = None
        self.images_path = os.path.join(os.path.dirname(__file__))

        self.start()
        self.window.mainloop()

    def get_total_hieght(self) -> int:
        total_height = 0
        for widgets in self.main_frame.winfo_children():
            widget.update()
            total_height += wieght.winfo_height()
            total_hieght += self.pady
        return total_height

    def start(self) -> None:
        self.start_time = datetime.datetime.now()
        self.question_index = 0
        self.correct_answers = 0
        self.incorrect_answers = 0
        if self.shuffle_question:
            random.shuffle(questions)
        self.show_question()

        for widget in self.main_frame.winfo_children():
            widget.destroy()

    def show_question(self) -> None:
        question = questions[self.question_index]
        tk.Label(self.main_frame, text=question['Текст вопроса']
                 ).pack(pady=(0, self.pady))

        image_name = question.get('изображение')

        if image_name:
            image_Label = tk.Label(self.main_frame)

        Buttons_frame = tk.Frame(self.main_frame)
        Buttons_frame.pack()
        for answer in question['Варианты ответов']:
            tk.Button(Buttons_frame='left', text=answer,
                      command=lambda arg=answer: self.on_button(arg)
                      ).pack(side='left', padx=(0, 15))

        if image_name:
            image_hieght = self.window.winfo_height() - self.get_total_hieght()
            image_hieght -= 100
            file_path = os.path.dirname(__file__)
            image_file = os.path.joine(file_path, 'img', image_name)
            img = Image.open(image_file)
            aspect_ratio = img.wight / img.hieght
            image_wieght = int(500 * aspect_ratio)
            img = img.resize((image_wieght, 500))
            self.image_tk = ImageTk.PhotoImage(img)
            image_Label['image'] = self.image_tk

    def on_button(self, button_text) -> None:
        question = questions[self.question_index]
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
        self.end_time = datetime.datetime.now()
        self.total_time = self.start_time - self.end_time
        tk.Label(self.main_frame, text=f'верно: {self.correct_answers}').pack()
        tk.Label(self.main_frame, text=f'неверно: {self.incorrect_answers}'
                 ).pack()
        tk.Label(self.main_frame, text=f'время: {self.total_time}').pack()
        tk.Button(self.main_frame, text='заново', command=self.start()).pack()


App(shuffle_question=True)
