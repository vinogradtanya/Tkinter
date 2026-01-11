from tkinter import *

from tkinter import filedialog as fd

def insertText():
    file_name = fd.askopenfilename()
    if not file_name:
        return
    try:
        with open(file_name, 'r', encoding='utf-8') as f:
            s = f.read()
    except UnicodeDecodeError:
        # Если UTF-8 не подошёл — пробуем cp1251 (для Windows-файлов)
        with open(file_name, 'r', encoding='cp1251') as f:
            s = f.read()
    text.delete(1.0, END)
    text.insert(1.0, s)

def extractText():  #Получаем имя файла, в который надо сохранить информацию
    file_name =fd.asksaveasfilename(filetypes=(("TXT files","*.txt"),
                                               ("HTML files", "*.html;*.htm"),
                                               ("All files", "*.*") ))
    f = open(file_name, 'w') #Открываем файл для записи
    s = text.get(1.0, END) #Считываем информацию из текстового поля
    f.write(s) #Записываем считанную информацию в файл
    f.close() #Закрываем файл

window = Tk() #Создаем окно
text = Text(width=50, height=25)
text.grid(columnspan=2)
b1 = Button(text="Открыть", command=insertText)
b1.grid(row=1,sticky=E)
b2 = Button(text="Сохранить", command=extractText)
b2.grid(row=1, column=1, sticky=W)
#Цикл обработки событий окна
window.mainloop()
