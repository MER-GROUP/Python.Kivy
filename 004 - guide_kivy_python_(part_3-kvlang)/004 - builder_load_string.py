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
# Класс Builder - закрузчик языка KV Lang
from kivy.lang.builder import Builder
# *****************************************************************************************
# Так же с помощью метода load_string попробуем написать разметку напрямую:
example_kv = Builder.load_string(
'''
#:kivy 2.0.0
BoxLayout:
    orientation: 'horizontal'
    Button:
        text: 'Click'
'''
)
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