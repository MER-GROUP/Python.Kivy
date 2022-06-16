# *****************************************************************************************
# Первое приложение c Kv Design Language
# Напишем первое приложение с Kv Design Language. 
# Для начала создадим файл myapp.py, где напишем такой код:
# *****************************************************************************************
# главное окно программы
from kivy.app import App
# Коробочный макет
from kivy.uix.boxlayout import BoxLayout
# *****************************************************************************************
# Пустой класс для которого будем создавать разметку 
# с помощью Kivy Design Language.
# Данный класс наследуется от макета Box Layout
class Example(BoxLayout):
    '''root widget'''
    pass
# *****************************************************************************************
# окно программы
# Основной класс с методом build который возвращает 
# экземляр класса Example
class HelloApp(App):
    # ---------------------------------------------------------------------------
    '''app widget'''
    # ---------------------------------------------------------------------------
    def build(self):
        example = Example()
        return example
    # ---------------------------------------------------------------------------
# *****************************************************************************************
# запуск программы
if __name__ == '__main__':
    HelloApp().run()
# *****************************************************************************************