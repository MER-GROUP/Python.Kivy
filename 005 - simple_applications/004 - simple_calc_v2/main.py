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
    # 6. привоить переменной previous_operand знак operand
    # 7. помечаем operand равным 'w' - был ввод чисел
    # 8. выполнить математические вычисления калькулятора
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
            self.previous_operand = self.operand # 6
            self.operand = 'w' # 7
            self.__calc() # 8

        # test
        print('write self.first_number =', self.first_number)##########
        print('write self.temp_number =', self.temp_number)##########
        print('write self.result_number =', self.result_number)##########
        print('write self.operand =', self.operand)##########
        print('write self.previous_operand =', self.previous_operand)##########
    # ---------------------------------------------------------------------------
    # математические вычисления калькулятора
    # 1. если operand не None то продолжить
    # 2. если operand равен 'w' и previous_operand равен None
    # (вводились только числа float)
    # то переменной result_number присвоить введенное число
    # 3. если operand равен 'w' и previous_operand равен '+'
    # то выполнить операцию сложения
    # 4. если operand равен '<' и previous_operand равен None
    # то обновить перменную result_number числом float
    def __calc(self):
        if self.operand is not None: # 1
            if ('w' == self.operand) and (self.previous_operand is None): # 2
                self.result_number = float(self.first_number)
            elif ('w' == self.operand) and ('+' == self.previous_operand): # 3
                self.result_number += float(self.first_number) - self.temp_number
                self.temp_number = float(self.first_number)
            elif ('<' == self.operand) and (self.previous_operand is None): # 4
                self.result_number = float(self.first_number)
                print("('<' == self.operand) and (self.previous_operand is None)")

        # test
        print('__calc self.operand =', self.operand)
        print('__calc self.previous_operand =', self.previous_operand)
        print('__calc self.first_number =', self.first_number)##########
        print('__calc self.temp_number =', self.temp_number)##########
        print('__calc self.result_number =', self.result_number)##########
        print('__calc self.operand =', self.operand)##########
    # ---------------------------------------------------------------------------
    # операнд сложения чисел
    # 1. если не было ввода цифр то nothing
    # 2. если operand равен '=' и previous_operand равен 'w' то nothing
    # то начать новую историю label_display_comment c ответа калькулятора
    # 3. обнулить temp_number
    # 4. метка display_clear - очистить дисплей когда начнешь ввод чисел 
    # 5. привоить переменной previous_operand знак operand
    # 6. привоить переменной operand знак '+'

    # 7. если operand равен '+' и previous_operand равен '+' то nothing
    # иначе записать историю в label_display_comment
    def add(self):
        if (self.first_number is None): # 1
            return
        if ('=' == self.operand) and ('w' == self.previous_operand): # 2
            self.label_display_comment.text = str(self.label_display_comment.text.split('=')[-1])

        self.temp_number = float() # 3
        self.display_clear = True # 4         
        self.previous_operand = self.operand # 5
        self.operand = '+' # 6

        if ('+' == self.operand) and ('+' == self.previous_operand): # 7
            return
        else:
            self.label_display_comment.text += str(self.operand)

        # test
        print('add self.first_number =', self.first_number)##########
        print('add self.temp_number =', self.temp_number)##########
        print('add self.result_number =', self.result_number)##########
        print('add self.operand =', self.operand)##########
        print('add self.previous_operand =', self.previous_operand)##########
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
    # ---------------------------------------------------------------------------
    # back - удаление цифр с конца
    # 1. previous_operand равен None
    # то удалить цимвол с конца числа
    # и обновить историю label_display_comment
    # также обновить operand
    # выполнить математические вычисления калькулятора 
    
    def back(self):
        if (self.previous_operand is None): # 1
            self.label_display.text = self.label_display.text[: -1]
            self.label_display_comment.text = self.label_display.text
            self.label_display.text = str('0')
            self.first_number = self.label_display.text
            self.__calc()    

        self.previous_operand = self.operand # 
        self.operand = '<' # 


        # test
        print('back self.first_number =', self.first_number)##########
        print('back self.temp_number =', self.temp_number)##########
        print('back self.result_number =', self.result_number)##########
        print('back self.operand =', self.operand)##########
        print('back self.previous_operand =', self.previous_operand)##########
    # ---------------------------------------------------------------------------
    # операнд равно (результат действий калькулятора)
    # 1. если operand равен None и previous_operand равен None то nothing
    # 2. если operand равен 'w' и previous_operand равен None то nothing
    # 2. если operand равен 'w' и previous_operand равен 'w' то nothing
    # 3. если operand равен '=' и first_number равен None то nothing
    # 4. если operand равен '=' и previous_operand равен 'w' то nothing
    # 5. если operand равен '+' и previous_operand равен '=' то nothing
    # 6. если first_number не None и operand не None и operand равен 'w'
    # и previous_operand равен '+' то показать ответ сложения
    # и записать в историю
    def equal(self):
        if (self.operand is None) and (self.previous_operand is None): # 1
            return
        if ('w' == self.operand) and (self.previous_operand is None): # 2
            return
        if ('w' == self.operand) and ('w' == self.previous_operand): # 3
            return
        if ('=' == self.operand) and (self.first_number is None): # 4
            return
        if ('=' == self.operand) and ('w' == self.previous_operand): # 5
            return
        if ('+' == self.operand) and ('=' == self.previous_operand): # 6
            return

        if ( # 7
            (self.first_number is not None) 
            and (self.operand is not None) 
            and (self.operand == 'w')
            and (self.previous_operand == '+')
            ):
            self.label_display.text = str(self.result_number)
            self.label_display_comment.text += str('=')
            self.label_display_comment.text += str(self.result_number)
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

        self.previous_operand = self.operand # 
        self.operand = '=' # 

        # test
        print('equal self.first_number =', self.first_number)##########
        print('equal self.temp_number =', self.temp_number)##########
        print('equal self.result_number =', self.result_number)##########
        print('equal self.operand =', self.operand)##########
        print('equal self.previous_operand =', self.previous_operand)##########
    # ---------------------------------------------------------------------------
    # обнудить все переменные при нажатии кнопки 'C'
    def clear(self):
        self.label_display.text = ''
        self.label_display_comment.text = ''
        self.display_clear = False
        self.first_number = None
        self.temp_number = float()
        self.result_number = float()
        self.operand = None
        self.previous_operand = None
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