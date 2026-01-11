from tkinter import *

window = Tk()  # создаём окно

window.title("Вывод текста")  # создаём заголовок окна

window.geometry("500x300")  # задаём размеры окна

label_2 = Label(window, text='Python', bg='blue', fg='red',
              font=('Arial', 24, 'bold'))  # задаём шрифт как кортеж

# label_2.pack()  # размещаем метку в окне
#
# #Размещаем метку в окне по вертикали - посередине, по горизонтали - посередине
# label_2.pack(expand = 1)
# #Заполняем всё пространство по горизонтали
# label_2. pack(expand = 1, fill = X)
# #Заполняем всё пространство по обеим осям
# label_2.pack(expand = 1, fill = BOTH)
#Размещаем метку с текстом в левом верхнем углу
label_2.pack(anchor = NW)

window.mainloop()

