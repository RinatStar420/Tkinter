""" Выбор из списка.
При помощи виджета Listbox можно добовлять в приложение список элементов, предлагаемых пользователю для выбора.
Для создания объекта listbox используется конструкция Listbox(), которому в качестве аргумента передается имя
родительского контейнера и возможные опции"""
from tkinter import *
# Доступ модуля cgi
import tkinter.messagebox as box

# Подключение модуля для раоты с диалоговыми окнами и назначение псевдонима через as

window = Tk()
# Создание окна
window.title('Listbox Example')
# Создание загаловка окна
frame = Frame(window)
# Создание фрейма в который помещаются виджеты
listbox = Listbox(frame)
# Создание виджета listbox и его элементов
listbox.insert(1, 'HTML5 in easy steps')
# insert() добавляет элемент в список (в качестве аргумента передается порядковый номер и строка
listbox.insert(2, 'CSS3 in easy steps')
# insert() добавляет элемент в список (в качестве аргумента передается порядковый номер и строка
listbox.insert(3, 'JavaScript in easy steps')
# insert() добавляет элемент в список (в качестве аргумента передается порядковый номер и строка
# 3 элемента виджета listbox


def dialog():
    """ Функция вывода выбранных элементов списка"""
    box.showinfo('Selection', 'Your Choice: ' + listbox.get(listbox.curselection()))
    # showinfo() выводит ОК (информационное) восклицательный знак в кругу


btn = Button(frame, text='Choose', command=dialog)
# Кнопка для вызова функции
btn.pack(side=RIGHT, padx=5) # Размещение кнопки во фрейм с помощью side=
listbox.pack(side=LEFT) # Размещение списка во фрейм с помощью side=
frame.pack(padx=30, pady=30) # Указание разметки фрейма

window.mainloop()
