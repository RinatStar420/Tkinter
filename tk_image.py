""" tkinter позволяет работать с изображениями, которые будут выведены в виджеты, для этого используется конструктор
Photoimage(), который создает объект изображения(уазать в аргументах file='name-file')"""

from tkinter import *
# Добавление cgi
window = Tk()
# Создание окна
window.title('Image Example')
# Создание заголовка окна
img = PhotoImage(file='giphy.gif')
# Создание объекта изображения из файловой локальной сиситемы
label = Label(window, image=img, bg='yellow')
# bg - опция выбора цвет фона
# Создание объекта label для вывода картинки поверх желтого фона метки
small_img = PhotoImage.subsample(img, x=3, y=3)
# subsample() - метод для уменьшения изображения (указать в аргументах параметры дискритизации х=значение, у=значение)
# х=2, у=2 приведут к отбрасыванию каждого второго пиксела то есть изображение уменьшится в половину от оригинала
# Содание уменшеного объекта изображения
btn = Button(window, image=small_img)
# Создание кнопки вывода уменьшенного изображения
txt = Text(window, width=25, height=7)
# Создание текстового поля
txt.image_create('1.0', image=small_img)
# Встраивание изображение в текстовое поле
txt.insert('1.1', 'Python Fun!')
# Добавление строки после изображения
can = Canvas(window, width=100, height=100, bg='white')
# Создание элемента холста
can.create_image((50, 50), image=small_img)
# Помещение в него второго изображения
can.create_line(0, 0, 100, 100, width=25, fill='yellow')
# Создание диагональной линии поверх помещенного рисунка
label.pack(side=TOP)
btn.pack(side=LEFT)
txt.pack(side=LEFT)
can.pack(side=LEFT, padx=10)
# Добавление виджетов на окно
window.mainloop()
# Добавление цикла обработки



