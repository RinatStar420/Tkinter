""" Флажки.
Виджет Checkbutton обеспечивает добавление в графическое приложение одного элемента "флажок", который может быть
установлен (выбран) пользователем. Обычно испоьзуется группа таких флажков и пользователь может выбрать из этой группы
один или несколько.
Объект флажка создается пи помощи конструктора Checkbutton(), которому передается 5 аргументов:
Имя родительского контейнера(фрейма)
text='text'
Управляющая переменная-объект variable=имя-переменной
Значение для присваивания, если флажок установлен пользователем onvalue=значение
Значение для присваивания, если флажок не установлен пользователем offvalue=значение
"""
from tkinter import *
import tkinter.messagebox as box

window = Tk()
window.title('Check Button Example')
frame = Frame(window)

var_1 = IntVar()
var_2 = IntVar()
var_3 = IntVar()
# создание целочисленных переменных для хранения значения в зависимости от результата выбора пользователя
book_1 = Checkbutton(frame, text='HTML5', variable=var_1, onvalue=1, offvalue=0)
book_2 = Checkbutton(frame, text='CSS3', variable=var_2, onvalue=1, offvalue=0)
book_3 = Checkbutton(frame, text='JS', variable=var_3, onvalue=1, offvalue=0)


# Создание трёх виджетов флажков, значение которых будут заноситься в переменные объекты

def dialog():
    """ Функция отображающая текущий выбор пользователя"""
    str = 'Your Choice: '
    if var_1.get() == 1: str += '\nHTML5 in easy steps'
    if var_2.get() == 1: str += '\nCSS3 in easy steps'
    if var_3.get() == 1: str += '\nJavaScript in easy steps'
    box.showinfo('Selection', str)


btn = Button(frame, text='Choose', command=dialog)
# Создание кнопки вызова функции dialog

btn.pack(side=RIGHT)
# Размещение кнопки в фрейм
book_1.pack(side=LEFT)
# Размещение флага в фрейм
book_2.pack(side=LEFT)
# Размещение флага в фрейм
book_3.pack(side=LEFT)
# Размещение флага в фрейм
frame.pack(padx=30, pady=30)
# Установка положения фрейма

window.mainloop()
