# *****************************************************************************************
# Перевод килограммов в граммы
# *****************************************************************************************
# главное окно программы
from kivy.app import App
# коробочный макет
from kivy.uix.boxlayout import BoxLayout
# свойства объекта (виджета)
from kivy.properties import ObjectProperty
# *****************************************************************************************
# конфигурация приложения kv
from kivy.config import Config
# задаем размеры окна статически
Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '60')
# *****************************************************************************************
# Работа с директориями и файлами ОС
from os.path import dirname, join
# Работа с директориями и файлами ОС
from pathlib import Path
# Класс Builder - закрузчик языка KV Lang
from kivy.lang import Builder
# Builder.load_file(str(Path(join(dirname(__file__), './convert.kv'))))
# *****************************************************************************************
# Перед созданием данного приложения давайте сначало подумаем 
# какие виджеты нам понадобятся. А понадобятся нам:
# 1. Горизонтальный макет BoxLayout(у нас будет класс KgWeight наследоваться 
# от класса BoxLayout)
# 2. Виджет Text Input для ввода значения в кг
# 3. Виджет Label для отображения '='
# 4. Виджет Label для отображения грамм
# Итак создадим два файла kgapp.py для кода и kg.kv для разметки. 
# В коде для начала зададим размер окна 400х60 с помощью Config.set
# *****************************************************************************************
# Далее напишем класс KgWeight который будет наследоваться от BoxLayout. 
# Его мы так же объявим в разметке. В нем создадим две переменные kg_input 
# и gramm_result которым присвоем ObjectProperty(None) и так же потом 
# объявим их в разметке. Даллее напишем метод convert_to_gramm в котором 
# тексту Label(переменная gramm_result ) присваиваемм значение в граммах
class Convert(BoxLayout):
    # ---------------------------------------------------------------------------
    '''app widget'''
    # ---------------------------------------------------------------------------
    # vars
    kg_input = ObjectProperty(None)
    gramm_result = ObjectProperty(None)
    # ---------------------------------------------------------------------------
    # methods
    def convert_to_gramm(self):
        self.gramm_result.text = str(float(self.kg_input.text) * 1000)
    # ---------------------------------------------------------------------------
    pass
    # ---------------------------------------------------------------------------
# *****************************************************************************************
# Далее создадим класс KgApp который неаследуется от класса App и в 
# его методе build создадим экземпляр класса KgWeight который будет 
# называться kg_weight.
class ConvertApp(App):
    # ---------------------------------------------------------------------------
    '''app widget'''
    # ---------------------------------------------------------------------------
    def build(self):
        return Convert()
    # ---------------------------------------------------------------------------
# *****************************************************************************************
# запуск программы
if __name__ == '__main__':
    ConvertApp().run()
# *****************************************************************************************