from tkinter import *

window = Tk()  # создаём окно

window.title("Изменение свойств")  # создаём заголовок окна

window.geometry("500x300")  # задаём размеры окна

# создаём кнопку
button = Button(window, bg='blue', fg='red', text='запуск программы',
                font='Arial 16')  # задаём свойства

# функция для изменения свойств кнопки
def change():  # задаём св-ва кнопки как элементы словаря
    button['text'] = 'Программа запущена'
    button['bg'] = '#000000'
    button['fg'] = '#ffffff'

# связываем кнопки с фун-й-обработчиком событий
button.configure(command=change)  # изменяем св-ва кнопки с помощью метода

# размещаем кнопки в окне
button.pack()

window.mainloop()