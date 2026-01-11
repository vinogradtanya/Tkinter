from tkinter import *

import tkinter.messagebox as box

def dialog():
    var = box.askyesno("Выбор действий", "Продолжаем вывод?")
    if var == 1:
        box.showinfo("Продолжение", "Продолжаем...")
    else:
        box.showwarning("прекращение", "Выход...")

window = Tk()  # создаём окно

window.title("Изменение свойств")  # создаём заголовок окна

window.geometry("500x300")  # задаём размеры окна

# создаём кнопку для выхода из программы
button_exit = Button(window, text='Выбор решения', bg='#ff0000', fg='green',
                font='Arial 16', command=dialog)

# размещаем кнопки в окне
button_exit.pack(padx=100, pady=100)

window.mainloop()