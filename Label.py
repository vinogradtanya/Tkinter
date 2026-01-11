from tkinter import *

window = Tk()  # создаём окно

window.title("Вывод текста")  # создаём заголовок окна

window.geometry("500x300")  # задаём размеры окна

# создаём первую метку
label = Label(window, text='Я учу язык программирования',
              font='Arial 16')  # задаём шрифт как строку

label.pack(side=TOP)  # размещаем метку в окне

# создаём вторую метку

label_2 = Label(window, text='Python',
              font=('Arial', 24, 'bold'))  # задаём шрифт как кортеж

label_2.pack(padx=150, pady=50)  # размещаем метку в окне

window.mainloop()