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
    # 1. очищаем дисплей если был нажат операнд
    def write_number(self, button):
        if not (self.operand == '='):
            # 1
            try:
                if (self.operand in '+-*/'):
                    self.label_display.text = ''
            except (TypeError):
                pass

            digit_begin = button.text

            if (chr(183) == digit_begin):
                digit_begin = '.'

            digit_end = self.label_display.text + digit_begin

            try:
                # if float(digit_end):
                if float(digit_end) or (digit_begin in '0.'):
                    # self.label_display.text += instance.text
                    # self.label_display.text += button.text
                    self.label_display.text += digit_begin
                    if (self.first_number is None):
                        self.first_number = 'first'
                    print('!!!self.first_number =', self.first_number)##########
            except (ValueError):
                return
    # ---------------------------------------------------------------------------
    # операнд сложения чисел
    def add(self):
        # если число не вводилась
        if (self.first_number is None):
            return
        # если был нажат операнд =
        # то абнуляем переменную operand
        if (self.operand == '='):
            self.operand = None
        # если был нажат любой операнд
        # if (self.operand is not None):
        #     return  
        # если был нажат любой операнд
        try:
            if (self.label_display_comment.text[-1] not in '+-*/'):
                return
        except (IndexError):
            pass

        # если дисплей калькулятора пустой
        # то ничего не делаем и историей label_display_comment
        # иначе записываем историю label_display_comment
        if ('' == self.label_display.text):
            self.label_display_comment.text += ''
        else:
            self.label_display_comment.text += str(float(self.label_display.text))
        
        # если число введено в первый раз
        # то обновляем перемееную first_number
        # если дисплей пуст то ничего не делаем
        # иначе производим действия с переменной first_number
        if 'first' == self.first_number:
            self.first_number = float(self.label_display.text)
        elif '' == self.label_display.text:
            pass
        else:
            self.first_number += float(self.label_display.text)  

        # делаем дисплей пустым    
        # self.label_display.text = ''
        # присваиваем переменной operand действие '+'
        self.operand = '+'

        # если операнд операнд не нажимался 
        # то обновить историю label_display_comment 
        if self.label_display_comment.text[-1] not in '+-*/':
            self.label_display_comment.text += str(self.operand)

        print('!!!self.first_number =', self.first_number)########## 
    # ---------------------------------------------------------------------------
    # операнд вычитания чисел
    def subtract(self):
        # если число не вводилась
        if (self.first_number is None):
            return
        # если был нажат операнд =
        # то абнуляем переменную operand
        if (self.operand == '='):
            self.operand = None
        # если был нажат любой операнд
        # if (self.operand is not None):
        #     return  
        # если был нажат любой операнд
        try:
            if (self.label_display_comment.text[-1] not in '+-*/'):
                return
        except (IndexError):
            pass

        # если дисплей калькулятора пустой
        # то ничего не делаем и историей label_display_comment
        # иначе записываем историю label_display_comment
        if ('' == self.label_display.text):
            self.label_display_comment.text += ''
        else:
            self.label_display_comment.text += str(float(self.label_display.text))
        
        # если число введено в первый раз
        # то обновляем перемееную first_number
        # если дисплей пуст то ничего не делаем
        # иначе производим действия с переменной first_number
        if 'first' == self.first_number:
            self.first_number = float(self.label_display.text)
        elif '' == self.label_display.text:
            pass
        else:
            self.first_number -= float(self.label_display.text)  

        # делаем дисплей пустым    
        self.label_display.text = ''
        # присваиваем переменной operand действие '+'
        self.operand = '-'

        # если операнд операнд не нажимался 
        # то обновить историю label_display_comment 
        if self.label_display_comment.text[-1] not in '+-*/':
            self.label_display_comment.text += str(self.operand)

        print('!!!self.first_number =', self.first_number)########## 
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
    def equal(self):
        if (self.operand == '=') or (self.first_number is None):
            return
        if (
            (self.first_number is not None) 
            and (self.operand is not None) 
            and (self.operand == '+')
            ):
            print('!!!self.first_number =', self.first_number)##########
            self.label_display_comment.text += str(float(self.label_display.text))
            self.label_display.text = str(self.first_number + float(self.label_display.text))
            # self.label_display.text = str(self.first_number)
            self.label_display_comment.text += '='
            self.label_display_comment.text += str(self.label_display.text)
        elif (
            (self.first_number is not None) 
            and (self.operand is not None) 
            and (self.operand == '-')
            ):
            print('!!!self.first_number =', self.first_number)##########
            self.label_display_comment.text += str(float(self.label_display.text))
            self.label_display.text = str(self.first_number - float(self.label_display.text))
            # self.label_display.text = str(self.first_number)
            self.label_display_comment.text += '='
            self.label_display_comment.text += str(self.label_display.text)
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
        self.first_number = None
        self.operand = None
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