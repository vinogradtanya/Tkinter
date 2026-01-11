# функция, переключающая цвет окна с жёлтого на зелёный и обратно
def color_switch():
    if window.cget('bg') == 'yellow':  # получаем цвет фона с помощью метода
        window.configure(bg='green')  # цвет фона зелёный
    else:
        window['bg']  = 'yellow'  # цвет фона жёлтый

from tkinter import *

window = Tk()  # создаём окно

window.title("Изменение свойств")  # создаём заголовок окна

window.geometry("500x300")  # задаём размеры окна

# создаём кнопку для выхода из программы
button_exit = Button(window, bg='#ff0000', fg='green', text='Выход',
                font='Arial 16', command=exit)  # задаём свойства

# создаём кнопку для изменения цвета экрана
button_switch = Button(window, bg='blue', fg='red', text='Цвет окна',
                font='Arial 16', command=color_switch)  # задаём свойства


# размещаем кнопки в окне
button_exit.pack(padx=150, pady=50)
button_switch.pack(padx=150,pady=20)


window.mainloop()