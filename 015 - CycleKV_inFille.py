# импорт основного окна App
from kivy.app import App
# GridLayout - сеточный макет
from kivy.uix.gridlayout import GridLayout
# импорт модуля Строитель - загружает .kv файлы в проект
from kivy.lang import Builder
# закрузить файл
Builder.load_file('./015/Window.kv')

# создаем основное окно программы, наследуя App - основные свойства окна
class TestApp(App):
    def build(self):
        # встраиваем в основное окно объект Сеточный макет
        # дизайн и функционал основного окна
        return Window()

# создаем основной сеточный макет
# описание свойств класса - ./015/Window.kv
class Window(GridLayout):
    pass

# если программа не модуль, то выполнить
if __name__ == '__main__':
    # запускаем приложение
    TestApp().run()