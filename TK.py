import tkinter as tk
import random
import datetime
import question
import os

questions = question.questions

full_path = __file__
directory_path = os.path.dirname(full_path)

imags_path = os.path.join(directory_path, 'img')

imags_path = os.path.join(directory_path, '01.png')


window = tk.Tk()

photo_image = tk.PhotoImage(file=imags_path)

tk.Lable(window, image=photo_image).pack()

window.mainloop
print(directory_path)


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

        self.total_time = None
        self.start_time = None
        self.end_time = None
        self.images_path = os.path.join(os.path.dirname(__file__))

        self.start()
        self.window.mainloop()

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
        tk.Label(self.main_frame, text=question['Текст вопроса']).pack(pady=(0, 30))
        image_name = question.get('изображение')
        if image_name is not None:
            file = os.path.joine(self.images_path, image_name)
            photo_image = tk.PhotoImage(file=file)
            tk.Label(self.main_frame, image=photo_image).pack()
        Buttons_frame = tk.Frame(self.main_frame)
        Buttons_frame.pack()
        for answer in question['Варианты ответов']:
            tk.Button(Buttons_frame='left', text=answer, command=lambda arg=answer: self.on_button(arg)).pack(side='left', padx=(0, 15))

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
        tk.Label(self.main_frame, text=f'неверно: {self.incorrect_answers}').pack()
        tk.Label(self.main_frame, text=f'время: {self.total_time}').pack()
        tk.Button(self.main_frame, text='заново', command=self.start()).pack()


App(shuffle_question=True)
