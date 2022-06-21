# *****************************************************************************************
# Простой калькулятор
# *****************************************************************************************
# главное окно программы
from kivy.app import App
# коробочный макет
from kivy.uix.boxlayout import BoxLayout
# свойства объекта (виджета)
from kivy.properties import ObjectProperty
# *****************************************************************************************
# поток таймер
# from threading import Timer as timer
# *****************************************************************************************
# конфигурация приложения kv
from kivy.config import Config
# задаем размеры окна статически
Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '500')
# *****************************************************************************************
# Работа с директориями и файлами ОС
from os.path import dirname, join
# Работа с директориями и файлами ОС
from pathlib import Path
# Класс Builder - закрузчик языка KV Lang
from kivy.lang import Builder
# Builder.load_file(str(Path(join(dirname(__file__), './calc.kv'))))
# *****************************************************************************************
# Создадим простой калькулятор. Какие виджеты нам для этого нужно:
# 1.Вертикальный макет BoxLayout(у нас будет класс Calculator который 
# будет наследоваться от класса BoxLayout)
# 2.Виджет Label где будут отображаться числа
# 3.Нам нужен будет макет в виде таблицы GridLayout для кнопок
# (мы определим его в разметке)
# 4.Кнопки от 0 до 9
# 5.Кнопки с операциями '+', '-', '*', '/', '='
# 6.Кнопка 'C' для очистки текста у виджета Label
# Создадим два файла calcapp.py для кода и calc.kv для разметки. 
# Начнем с кода calcapp.py. Для начала зададим размер окна 400х500 
# с помощью Config.set
# *****************************************************************************************
# Далее создадим класс Calculator который будет наследоваться от 
# BoxLayout и который так же будет у нас в разметке. В нем объявим 
# переменную label которая так же будет у нас в разметке. 
# Так же объявим переменную first_number и будем присваивать 
# ей первое число, но в начале присвоем ей None. Так же создадим 
# переменную operand куда будет присваивать 
# операции '+', '-', '*', '/', '=', но в начале она будет равна None

# Начнем писать методы в этом классе. Первый метод write_number 
# который будет присвоен событию on_press кнопкам с числами в разметке. 
# При нажатию на кнопку с числом в нашем виджете Label будет 
# отображаться это число. Обратите внимание что в этом методе 
# вторым параметром после self идет instance. Параметр instance это 
# объект который вызывает этот метод. В нашем случае это нажатая кнопка. 
# Через instance мы будем обращаться к атрибуту text у кнопки. 
# Сначала в этом методе мы пишим условие что operand не равен знаку '='. 
# Если это так то переменной label(где отображаются числа) 
# мы присваиваем старое значение переменной label плюс 
# instance.text(число с кнопки). Далее в этом же условии пишем условие 
# что если переменная first_number равна None, то присвоим ей же значение 0
class Calc(BoxLayout):
    # ---------------------------------------------------------------------------
    '''root widget'''
    # ---------------------------------------------------------------------------
    # vars
    label = ObjectProperty(None)
    first_number = None
    operand = None
    # ---------------------------------------------------------------------------
    # methods
    # ---------------------------------------------------------------------------
    pass
    # ---------------------------------------------------------------------------
# *****************************************************************************************
class CalcApp(App):
    # ---------------------------------------------------------------------------
    '''app widget'''
    # ---------------------------------------------------------------------------
    def build(self):
        return Calc()
    # ---------------------------------------------------------------------------
# *****************************************************************************************
# запуск программы
if __name__ == '__main__':
    CalcApp().run()
# *****************************************************************************************