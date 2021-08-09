from tkinter import *

""" Работа с кнопками
Виджет Button - элемент графического окнного элемента 'кнопка'
Скрипт кнопки смены цвета фона """
# доступ к функии gui
window = Tk()
# Создание окна
window.title('Button Example')
# Создание загаловка для окна
btn_end = Button(window, text='Close', command=exit)


# Кнопка, при нажатию из которой происходит выход из программы

def tog():
    """ Функция переключатель цвета фона окна после нажатия еще одной кнопки """
    if window.cget('bg') == 'yellow':  # cget() - получение значения опций
        window.configure(bg='gray')  # bg - опция цвета фона
    else:
        window.configure(bg='yellow')


btn_tog = Button(window, text='Switch', command=tog)
# Кнопка по нажатию которой будет вызываться функция
btn_tog.pack(padx=150, pady=20)
btn_end.pack(padx=150, pady=20)
# Добавление кнопок на окно с указанием парметров заполнение по Х и У
window.mainloop()
# Цикл обработки событий
