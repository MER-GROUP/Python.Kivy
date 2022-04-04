# Коробочный макет - BoxLayout
# Сеточный макет - GridLayout
# Плавающий макет - FloatLayout
# инпорт констант
from tkinter import VERTICAL
from tkinter import HORIZONTAL
# импорт основного окна App
from kivy.app import App
# импорт модуля Коробочный макет
# в него будем пихать кнопки и др. GUI элементы
from kivy.uix.boxlayout import BoxLayout
# импорт модуля Кнопка
from kivy.uix.button import Button
# импорт модуля Рандом
# choice - возвращает одно случайное значение из спаска (массива)
from random import choice

# глобальные переменные 
# цвета для кнопок
# красный цвет
red = [1, 0, 0, 1]
# зеленый цвет
green = [0, 1, 0, 1]
# голубой цвет
blue = [0, 0, 1, 1]
# фиолетовый цвет
purple = [1, 0, 1, 1]

# создаем основное окно программы, наследуя App - основные свойства окна
class MainApp(App):
    # создаем стандартный конструктор Kivy: build(self)
    # где переопределяем некоторые стандартные свойства окна
    def build(self):
        # заголовок окна
        self.title = 'BoxLayout'
        # определякм объект BoxLayout
        # padding - расстояние границ между оъектами
        # padding: Вы можете указать padding в пикселях между макетом и его дочерними элементами одним из трех способов:
        # Список четыре-аргумента: [ padding_left, padding_top, padding_right, padding_bottom]
        # Список с двумя аргументами: [ padding_horizontal, padding_vertical]
        # Единственный аргумент: padding=10
        # spacing: Вы можете добавить пробел между дочерними виджетами с этим аргументом.
        # orientation: Вы можете изменить значение orientation по умолчанию BoxLayout с горизонтального на вертикальное.
        box = BoxLayout(padding=50, orientation=VERTICAL, spacing=10)
        # массив цветов
        colors = [red, green, blue, purple]
        # создадим 5 кнопок и добавим их в объект box
        # text - наименвание кнопки
        # background_color - фоновый цвет кнопки
        for i in range(5):
            btn = Button(text=f'Кнопка #{i +1}',
                            background_color=choice(colors))
            box.add_widget(btn)
        # встраиваем в основное окно объект Коробочный макет
        return box

# если программа не модуль, то выполнить
if __name__ == '__main__':
    # запускаем приложение
    MainApp().run()