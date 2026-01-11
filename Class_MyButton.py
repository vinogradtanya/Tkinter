from tkinter import *

class My_Button:
    # конструкор с аргументами
    def __init__(self, mwindow, mtext='Цвет окна', mwidth=15,
                 mheight=3, mfg='red', mbg='blue', mpdx=150, mpdy=50):
        # создаём кнопку с параметрами по умолчанию
        self.btn = Button(mwindow, text=mtext, width=mwidth, height=mheight,
                          bg=mbg, fg=mfg)
        self.btn.pack(padx=mpdx, pady=mpdy)

        # конфигурирование функции обработчика событий
    def setFunc(self, func):
        self.btn['command'] = eval('self.' + func)

        # функция, переключающая цвет окна с жёлтого на зелёный и обратно
    def color_change(self):
        if window.cget('bg') == 'yellow':  # получаем цвет фона с помощью метода
            window.configure(bg='green')  # цвет фона зелёный
        else:
            window['bg'] = 'yellow'  # цвет фона жёлтый

    def m_exit(self):
        exit()

window = Tk()  # создаём окно

window.title("Изменение свойств")  # создаём заголовок окна

window.geometry("500x300")  # задаём размеры окна

btn_switch = My_Button(window)
btn_switch.setFunc('color_change') # связываем кнопку с обработчиком событий
btn_exit = My_Button(window, "Выход", 12, 2, '#ff0000',
                     'green', 150, 20)
btn_exit.setFunc('m_exit')

window.mainloop()
