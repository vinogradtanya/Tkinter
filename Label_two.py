from tkinter import *

window = Tk()  # создаём окно

# создаём четыре кнопки
lab_1 = Label(width=8, height=3, bg='yellow', text='1')

lab_2 = Label(width=8, height=3, bg='red', text='2')

lab_3 = Label(width=8, height=3, bg='lightgreen', text='3')

lab_4 = Label(width=8, height=3, bg='lightblue', text='4')

# располагаем метки вертикально сверху вниз
lab_1.pack()
lab_2.pack()
lab_3.pack()
lab_4.pack()

# располагаем метки вертикально снизу вверх
# lab_1.pack(side=BOTTOM)
# lab_2.pack(side=BOTTOM)
# lab_3.pack(side=BOTTOM)
# lab_4.pack(side=BOTTOM)

# располагаем метки вертикально слева направо
# lab_1.pack(side=LEFT)
# lab_2.pack(side=LEFT)
# lab_3.pack(side=LEFT)
# lab_4.pack(side=LEFT)

# располагаем метки вертикально справа налево
# lab_1.pack(side=RIGHT)
# lab_2.pack(side=RIGHT)
# lab_3.pack(side=RIGHT)
# lab_4.pack(side=RIGHT)

window.mainloop()