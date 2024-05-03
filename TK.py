import tkinter as tk
import random
import datetime
import question

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

        self.question_index = None
        self.correct_answers = None
        self.incorrect_answers = None
        self.shuffle_question = None

        self.start_time = None
        self.end_time = None

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
        Buttons_frame = tk.Frame(self.main_frame)
        Buttons_frame.pack()
        for answer in question['Варианты ответов']:
            tk.Button(Buttons_frame='left', text=answer, command= lambda arg=answer: self.on_button(arg)).pack(side='left', padx=(0,15))

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
        total_time = self.start_time - self.end_time
        tk.Label(self.main_frame, text=f'верно: {self.correct_answers}').pack()
        tk.Label(self.main_frame, text=f'неверно: {self.incorrect_answers}').pack()
        tk.Label(self.main_frame, text=f'время: {self.total_time}').pack()
        tk.Button(self.main_frame, text='заново', command=self.start()).pack()




App(shuffle_question=True)