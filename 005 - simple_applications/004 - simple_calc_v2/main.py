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
    display_clear = False
    first_number = None
    temp_number = float()
    result_number = float()
    operand = None
    previous_operand = None
    # ---------------------------------------------------------------------------
    # methods
    # ---------------------------------------------------------------------------
    # нажатие цифровых кнопок и кнопки 'точка'
    # если число float то вводить цифры
    # иначе ничего не делать
    # def write_number(self, instance):
    # 1. если operand не равен '='
    # 2. очищаем дисплей если был нажат operand
    # 3. если введена '.' то digit_begin присваиваем '.'
    # 4. проверка на ввод float числа
    # 5. записываем цифры в label_display_comment
    # 6. помечаем operand равным 'w' - был ввод чисел
    def write_number(self, button): 
        if not (self.operand == '='): # 1

            if self.display_clear: # 2
                self.label_display.text = ''
                self.display_clear = False

            digit_begin = button.text # 3
            if (chr(183) == digit_begin):
                digit_begin = '.'

            digit_end = self.label_display.text + digit_begin # 4
            try: 
                if float(digit_end) or (digit_begin in '0.'):
                    self.label_display.text += digit_begin
                    self.first_number = self.label_display.text
            except (ValueError):
                return

            self.label_display_comment.text += str(self.first_number)[-1] # 5

            self.operand = 'w' # 6

            self.__calc()

            # test
            print('!!!self.first_number =', self.first_number)##########
            print('!!!self.temp_number =', self.temp_number)##########
            print('!!!self.result_number =', self.result_number)##########
            print('!!!self.operand =', self.operand)##########
    # ---------------------------------------------------------------------------
    #
    def __calc(self):
        # test
        print('__calc self.operand =', self.operand)
        print('__calc self.previous_operand =', self.previous_operand)
        print('__calc self.first_number =', self.first_number)##########
        print('__calc self.temp_number =', self.temp_number)##########
        print('__calc self.result_number =', self.result_number)##########
        print('__calc self.operand =', self.operand)##########

        if self.operand is not None:
            if ('w' == self.operand) and (self.previous_operand is None):
                self.result_number = float(self.first_number) ###
            elif ('w' == self.operand) and ('+' == self.previous_operand):
                # self.result_number += float(self.temp_number)
                self.result_number += float(self.first_number) - self.temp_number
                self.temp_number = float(self.first_number)
    # ---------------------------------------------------------------------------
    # операнд сложения чисел
    # 1. если не было ввода цифр то nothing
    # 2. обнулить temp_number
    def add(self):
        if (self.first_number is None): # 1
            return

        temp_number = float() # 2

        # test
        print('+++ add')

        # self.result_number = float(self.first_number)###
        # self.first_number = float(self.label_display.text)
        # self.label_display.text = ''
        self.display_clear = True
        # self.label_display_comment.text = str(float(self.label_display.text))
      
        self.operand = '+'
        self.previous_operand = self.operand

        self.label_display_comment.text += str(self.operand)

        # test
        print('+++self.first_number =', self.first_number)##########
        print('+++self.temp_number =', self.temp_number)##########
        print('+++self.result_number =', self.result_number)##########
        print('+++self.operand =', self.operand)##########
    # ---------------------------------------------------------------------------
    # операнд вычитания чисел
    def subtract(self):
        if (self.first_number is None):
            return
        if (self.operand == '='):
            self.operand = None
        if (self.operand is not None):
            return
        self.first_number = float(self.label_display.text)
        self.label_display.text = ''
        self.operand = '-'
    # ---------------------------------------------------------------------------
    def multiply(self):
        if (self.first_number is None):
            return
        if (self.operand == '='):
            self.operand = None
        if (self.operand is not None):
            return
        self.first_number = float(self.label_display.text)
        self.label_display.text = ''
        self.operand = '*'

    def division(self):
        if (self.first_number is None):
            return
        if (self.operand == '='):
            self.operand = None
        if (self.operand is not None):
            return
        self.first_number = float(self.label_display.text)
        self.label_display.text = ''
        self.operand = '/'

    # операнд равно (результат действий калькулятора)
    # 1. если operand равен '=' или first_number равен None то nothing
    # 2. __calc() - выполнить арифметические действия
    # 3. если first_number не None и operand не None и operand равен '+'
    # то показать ответ сложения
    def equal(self):
        if (self.operand == '=') or (self.first_number is None): # 1
            return
        self.__calc() # 2

        #
        if (
            (self.first_number is not None) 
            and (self.operand is not None) 
            and (self.operand == '+')
            ):
            # self.label_display.text = str(self.first_number + float(self.label_display.text))
            self.label_display.text = str(self.result_number)
            # self.label_display_comment += '='
            # self.label_display_comment += str(self.result_number)
        elif (
            (self.first_number is not None) 
            and (self.operand is not None) 
            and (self.operand == '-')
            ):
            self.label_display.text = str(self.first_number - float(self.label_display.text))
        elif (
            (self.first_number is not None) 
            and (self.operand is not None) 
            and (self.operand == '*')
            ):
            self.label_display.text = str(self.first_number * float(self.label_display.text))
        elif (
            (self.first_number is not None) 
            and (self.operand is not None) 
            and (self.operand == '/')
            and not ('0' == self.label_display.text)
            ):
            self.label_display.text = str(self.first_number // float(self.label_display.text))
        self.operand = '='

    def clear(self):
        self.display_clear = False
        self.first_number = None
        self.temp_number = float()
        self.result_number = float()
        self.operand = None
        self.previous_operand = None
        self.label_display.text = ''
        self.label_display_comment.text = ''
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