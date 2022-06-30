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
    write_number = None
    temp_number = float()
    result_number = float()
    operand = None
    previous_operand = None
    # ---------------------------------------------------------------------------
    # methods
    # ---------------------------------------------------------------------------
    # нажатие цифровых кнопок и кнопки 'точка'
    # 1. если дисплей не очищен то очистить
    # (указывать в операндах self.display_clear = True)
    # 2. проверка числа на float
    # (проверки если были первыми введены знаки '-', '.', '0')
    # 3. проверка числа на float через исключение
    # 4. записываем проверенное число на дисплей калькулятора
    # 5. записываем в переменную write_number итоговое введенное проверенное число
    # 6. записываем историю ввода чисел в переменную label_display_comment
    # 7. записываем в переменную previous_operand предыдущий операнд
    # 8. записываем в переменную operand текущий операнд
    def write_digit(self, button): 
        if self.display_clear: # 1
            self.label_display.text = ''
            self.display_clear = False

        digit_begin = button.text # 2
        if ('-' == digit_begin) and ('' == self.label_display.text):
            digit_begin = '-0'
        elif ((2 == len(self.label_display.text))
            and ('-0' == self.label_display.text)
            ):
            digit_begin = '-' + digit_begin
            self.label_display.text = ''
        elif (('0' == digit_begin) 
            and ('' != self.label_display.text)
            and (1 == len(self.label_display.text)) 
            and ('0' == self.label_display.text[0])
            ):
            return
        elif (chr(183) == digit_begin) and (0 == len(self.label_display.text)):
            digit_begin = '0.'
        elif (chr(183) == digit_begin):
            digit_begin = '.'

        digit_end = self.label_display.text + digit_begin # 3
        try: 
            if float(digit_end):
                pass 
            else:
                pass          
        except (ValueError):
            return

        self.label_display.text += digit_begin # 4
        self.write_number = digit_end # 5

        if (('' != self.label_display.text) # 6
            and (('-' == self.label_display.text[0]) or ('0.' == self.label_display.text))
            and (2 == len(self.label_display.text))
            ):
            self.label_display_comment.text = str(self.write_number)
        else:
            self.label_display_comment.text += str(self.write_number)[-1]
    
        self.previous_operand = self.operand # 7
        self.operand = 'w' # 8
    # ---------------------------------------------------------------------------
    # операнд сложения чисел
    def add(self):
        self.previous_operand = self.operand
        self.operand = '+'
    # ---------------------------------------------------------------------------
    # операнд вычитания чисел
    def subtract(self):
        self.previous_operand = self.operand
        self.operand = '-'
    # ---------------------------------------------------------------------------
    # операнд умножения чисел
    def multiply(self):
        self.previous_operand = self.operand
        self.operand = '*'
    # ---------------------------------------------------------------------------
    # операнд деления чисел
    def division(self):
        self.previous_operand = self.operand
        self.operand = '/'
    # ---------------------------------------------------------------------------
    # операнд удаление чисел 
    def back(self):
        self.previous_operand = self.operand
        self.operand = 'b'
    # ---------------------------------------------------------------------------
    # операнд равно (результат действий калькулятора)
    def equal(self):
        self.previous_operand = self.operand
        self.operand = '='
    # ---------------------------------------------------------------------------
    # обнудить все переменные при нажатии кнопки 'C'
    def clear(self):
        self.label_display.text = ''
        self.label_display_comment.text = ''
        self.display_clear = False
        self.write_number = None
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
    title = 'Simple Calc v3.0'
    def build(self):
        return Calc()
    # ---------------------------------------------------------------------------
# *****************************************************************************************
# запуск программы
if __name__ == '__main__':
    CalcApp().run()
# *****************************************************************************************