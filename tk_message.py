""" Вывод сообщений в диалоговом окне с помощью методов модуля tkinter.messagebox """
from tkinter import *
# Доступ к модулю gui
import tkinter.messagebox as box

# Доступ к модулю messagebox с присвоением псевдонима через as
window = Tk()
# Создание окна
window.title('Button Example')


# Создание загаловка окна

def dialog():
    """ Функция вывода различных диалоговых окнон """
    var = box.askyesno('Message Box', 'Proceed?')
    # askyesno Yes(возвращает 1) и No
    if var == 1:
        box.showinfo('Yes Box', 'Proceeding...')
        # showinfo() выводит ОК (информационное) восклицательный знак в кругу
    else:
        box.showwarning('No Box', 'Cancelling...')
        # showwarning() выводит ОК (предупреждающее) восклицательный знак в треугольнике


btn = Button(window, text='Click', command=dialog)
# Кнопка при нажатии которой вызывается функция
btn.pack(padx=150, pady=50)
# Добавление кноки на окно и указание параметров заполнение
window.mainloop()
