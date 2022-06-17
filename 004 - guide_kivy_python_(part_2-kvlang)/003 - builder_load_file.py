# *****************************************************************************************
# Класс Builder
# Модуль: kivy.lang.builder
# Класс Builder позволяет загружать файл Kv Design Language,
# а так же с помощью метода load_string напрямую писать разметку.

# Методы
# load_file('путь к файлу') - позволяет загружать файл с расширением ".kv".
# load_string("""разметка""") - в качестве параметра пишем разметку 
# Kv Design Language.
# *****************************************************************************************
# главное окно программы
from kivy.app import App
# Работа с директориями и файлами ОС
from os.path import dirname, join
# Работа с директориями и файлами ОС
from pathlib import Path
# Класс Builder - закрузчик языка KV Lang
from kivy.lang.builder import Builder
# *****************************************************************************************
# Создадим файл builder_app.py и загрузим нашу разметку example.kv 
# с помощью метода load_file и присвоем переменной example_kv:
example_kv = Builder.load_file(str(Path(join(dirname(__file__), './003 - buider_load_file.kv'))))
# *****************************************************************************************
class BuilderApp(App):
    # ---------------------------------------------------------------------------
    '''app widget'''
    # ---------------------------------------------------------------------------
    def build(self):
        return example_kv
    # ---------------------------------------------------------------------------
# *****************************************************************************************
# запуск программы
if __name__ == '__main__':
    BuilderApp().run()
# *****************************************************************************************