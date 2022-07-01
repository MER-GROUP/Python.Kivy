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
    calc_arr = list()
    # ---------------------------------------------------------------------------
    # methods
    # ---------------------------------------------------------------------------
    # нажатие цифровых кнопок и кнопки 'точка'
    # 1. если дисплей не очищен то очистить
    # (указывать в операндах self.display_clear = True)
    # 2. проверка числа на float
    # (проверки если были первыми введены знаки '-', '.', '0', '00', '01' и тд.)
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
            and ('0' == digit_begin)
            ):
            return
        elif ((2 == len(self.label_display.text))
            and ('-0' == self.label_display.text)
            and (chr(183) != digit_begin)
            ):
            digit_begin = '-' + digit_begin
            self.label_display.text = ''
        elif ((2 == len(self.label_display.text))
            and ('-0' == self.label_display.text)
            and (chr(183) == digit_begin)
            ):
            digit_begin = '-0.'
            self.label_display.text = digit_begin
        elif ((('0' == digit_begin) or (chr(183) != digit_begin))
            and ('' != self.label_display.text)
            and (1 == len(self.label_display.text)) 
            and ('0' == self.label_display.text[0])
            ):
            return
        elif (chr(183) == digit_begin) and (0 == len(self.label_display.text)):
            digit_begin = '0.'
        elif (chr(183) == digit_begin):
            digit_begin = '.'

        if ('-0.' == digit_begin): # 3
            digit_end = self.label_display.text
        else:
            digit_end = self.label_display.text + digit_begin 
        try: 
            if float(digit_end):
                pass 
            else:
                pass          
        except (ValueError):
            # test
            print('------------------------------------------------')
            print('!!!!!!!!!!!!!!!!!!! EXCEPTION !!!!!!!!!!!!!!!!!!')
            print(f'!!!!!!!!!!!!digit_end = {digit_end}!!!!!!!!!!!!')
            return

        if ('-0.' == digit_begin): # 4
            self.label_display.text = digit_begin
        else:
            self.label_display.text += digit_begin 
        self.write_number = digit_end # 5

        if (('' != self.label_display.text) # 6
            and (('-' == self.label_display.text[0]) 
                or ('0.' == self.label_display.text))
            and (2 == len(self.label_display.text))
            ):
            print('IF 111111') #########12121212121211212!!!!!!!!!!!! написать парсинг
            self.label_display_comment.text = str(self.write_number)
        elif (('' != self.label_display.text)
            and ('-0.' == self.label_display.text)
            and (3 == len(self.label_display.text))
            ):
            print('IF 222222') #########12121212121212121!!!!!!!!!!!! написать парсинг
            self.label_display_comment.text = str(self.write_number)
        else:
            self.label_display_comment.text += str(self.write_number)[-1]
    
        self.previous_operand = self.operand # 7
        self.operand = 'w' # 8

        # test
        print('------------------------------------------------')
        print(' write write_number =', self.write_number)
        print(' write temp_number =', self.temp_number)
        print(' write result_number =', self.result_number)
        print(' write operand =', self.operand)
        print(' write previous_operand =', self.previous_operand)
        print(' write calc_arr =', self.calc_arr)
        print(' write digit_end =', digit_end)
    # ---------------------------------------------------------------------------
    # операнд сложения чисел
    # 1. пометить переменную display_clear в True
    # (при следующем вводе цифр очистить дисплей калькулятора)

    # ?. записываем в переменную previous_operand предыдущий операнд
    # ?. записываем в переменную operand текущий операнд

    # ?. записываем историю в label_display_comment

    # ?. записать в список (массив) итоговую переменную write_number и примененный operand
    def add(self):
        self.display_clear = True # 1

        self.previous_operand = self.operand # ?
        self.operand = '+' # ?

        self.label_display_comment.text += str(self.operand) # ?

        self.calc_arr.append(self.write_number) # ?
        self.calc_arr.append(self.operand)

        # test
        print('------------------------------------------------')
        print(' add write_number =', self.write_number)
        print(' add temp_number =', self.temp_number)
        print(' add result_number =', self.result_number)
        print(' add operand =', self.operand)
        print(' add previous_operand =', self.previous_operand)
        print(' add calc_arr =', self.calc_arr)
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
    # 1. удалить крайнюю цифру из числа
    # 2. записываем в переменную previous_operand предыдущий операнд
    # 3. записываем в переменную operand текущий операнд
    def back(self):
        if ('' != self.label_display.text): # 
            self.label_display.text = self.label_display.text[: -1]
            self.write_number = None if 0 == len(self.label_display.text) else self.label_display.text
            self.label_display_comment.text = self.label_display_comment.text[: -1]
        elif (self.label_display.text is None):
            self.label_display.text = ''
        else:
            return

        self.previous_operand = self.operand # 2
        self.operand = 'b' # 3

        # test
        print('------------------------------------------------')
        print(' back write_number =', self.write_number)
        print(' back temp_number =', self.temp_number)
        print(' back result_number =', self.result_number)
        print(' back operand =', self.operand)
        print(' back previous_operand =', self.previous_operand)
        print(' back calc_arr =', self.calc_arr)
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
        calc_arr = list()

        # test
        print('------------------------------------------------')
        print(' clear write_number =', self.write_number)
        print(' clear temp_number =', self.temp_number)
        print(' clear result_number =', self.result_number)
        print(' clear operand =', self.operand)
        print(' clear previous_operand =', self.previous_operand)
        print(' clear calc_arr =', self.calc_arr)
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