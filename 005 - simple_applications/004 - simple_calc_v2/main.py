# *****************************************************************************************
# Простой калькулятор
# *****************************************************************************************
# главное окно программы
from kivy.app import App
# коробочный макет
from kivy.uix.boxlayout import BoxLayout
# свойства объекта (виджета)
from kivy.properties import ObjectProperty
# определение ОС
from kivy.utils import platform
# *****************************************************************************************
if not 'android' == platform:
    # конфигурация приложения kv
    from kivy.config import Config
    # задаем размеры окна статически
    Config.set('graphics', 'width', '300')
    Config.set('graphics', 'height', '300')
    # запрещаем изменение размеров окна
    Config.set('graphics','resizable', False)
# *****************************************************************************************
# Работа с директориями и файлами ОС
# listdir - показывает файлы в конкретной папке
from os import listdir
# Работа с директориями и файлами ОС
from os.path import dirname, join
# Работа с директориями и файлами ОС
from pathlib import Path
# Класс Builder - закрузчик языка KV Lang
from kivy.lang import Builder
# Builder.load_file(str(Path(join(dirname(__file__), './design/'))))
# записываем директорию в переменную kv_path
folder = './design/'
kv_path = str(Path(join(dirname(__file__), folder)))
# загрузить все файлы .kv по отдельности
for file in listdir(kv_path):
    kv_path_file = str(Path(join(kv_path, file)))
    Builder.load_file(kv_path_file)
# *****************************************************************************************
# Действия программы
class Calc(BoxLayout):
    # ---------------------------------------------------------------------------
    '''root widget'''
    # ---------------------------------------------------------------------------
    # vars
    # ---------------------------------------------------------------------------
    label_display = ObjectProperty(None)
    label_display_comment = ObjectProperty(None)
    first_number = None
    operand = None
    # ---------------------------------------------------------------------------
    # methods
    # ---------------------------------------------------------------------------
    # нажатие цифровых кнопок и кнопки 'точка'
    # если число float то вводить цифры
    # иначе ничего не делать
    # def write_number(self, instance):
    def write_number(self, button):
        if not (self.operand == '='):
            digit_begin = button.text

            if (chr(183) == digit_begin):
                digit_begin = '.'

            digit_end = self.label_display.text + digit_begin
            try:
                if float(digit_end):
                    # self.label_display.text += instance.text
                    # self.label_display.text += button.text
                    self.label_display.text += digit_begin
                    if (self.first_number is None):
                        self.first_number = 0
            except (ValueError):
                return
    # ---------------------------------------------------------------------------
    def add(self):
        if (self.first_number is None):
            return
        if (self.operand == '='):
            self.operand = None
        if (self.operand is not None):
            return
        self.first_number = int(self.label_display.text)
        self.label_display.text = ''
        self.operand = '+'

    def subtract(self):
        if (self.first_number is None):
            return
        if (self.operand == '='):
            self.operand = None
        if (self.operand is not None):
            return
        self.first_number = int(self.label_display.text)
        self.label_display.text = ''
        self.operand = '-'

    def multiply(self):
        if (self.first_number is None):
            return
        if (self.operand == '='):
            self.operand = None
        if (self.operand is not None):
            return
        self.first_number = int(self.label_display.text)
        self.label_display.text = ''
        self.operand = '*'

    def division(self):
        if (self.first_number is None):
            return
        if (self.operand == '='):
            self.operand = None
        if (self.operand is not None):
            return
        self.first_number = int(self.label_display.text)
        self.label_display.text = ''
        self.operand = '/'

    def equal(self):
        if (self.operand == '=') or (self.first_number is None):
            return
        if (
            (self.first_number is not None) 
            and (self.operand is not None) 
            and (self.operand == '+')
            ):
            self.label_display.text = str(self.first_number + int(self.label_display.text))
        elif (
            (self.first_number is not None) 
            and (self.operand is not None) 
            and (self.operand == '-')
            ):
            self.label_display.text = str(self.first_number - int(self.label_display.text))
        elif (
            (self.first_number is not None) 
            and (self.operand is not None) 
            and (self.operand == '*')
            ):
            self.label_display.text = str(self.first_number * int(self.label_display.text))
        elif (
            (self.first_number is not None) 
            and (self.operand is not None) 
            and (self.operand == '/')
            and not ('0' == self.label_display.text)
            ):
            self.label_display.text = str(self.first_number // int(self.label_display.text))
        self.operand = '='

    def clear(self):
        self.first_number = None
        self.operand = None
        self.label_display.text = ''
    # ---------------------------------------------------------------------------
    pass
    # ---------------------------------------------------------------------------
# *****************************************************************************************
# Окно программы
class CalcApp(App):
    # ---------------------------------------------------------------------------
    '''app widget'''
    # ---------------------------------------------------------------------------
    title = 'Simple Calc v2.0'
    def build(self):
        return Calc()
    # ---------------------------------------------------------------------------
# *****************************************************************************************
# запуск программы
if __name__ == '__main__':
    CalcApp().run()
# *****************************************************************************************