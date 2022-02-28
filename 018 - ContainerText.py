# *****************************************************************************************
# импорт основного окна App
from kivy.app import App
# импорт модуля Коробочный макет
# в него будем пихать кнопки и др. GUI элементы
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
# импортируем модуль Свойство Объекта 
# для работы с переменными (свойствами) KV файлав
from kivy.properties import ObjectProperty
# импорт модуля Строитель - загружает .kv файлы в проект
from kivy.lang import Builder
# *****************************************************************************************
# создаем основное окно программы, наследуя App - основные свойства окна
class Programm(App):
    # создаем стандартный конструктор Kivy: build(self)
    def build(self):
        # встраиваем дизайн и функционал основного окна
        return BoxLayoutDecor()
# *****************************************************************************************
# декоратор - коробочный макет
class BoxLayoutDecor(BoxLayout):
    # доступ с переменным и свойствам класса в KV файлах
    container = ObjectProperty(None)

    # метод - прокрутка экранов
    def next_screen(self, screen):
        # определение имени KV файла
        filename = screen + '.kv'
        # выгрузить содержимое файла .kv
        # причина: в нем могут быть данные из предыдущих вызовов
        # unload the content of the .kv file
        # reason: it could have data from previous calls
        Builder.unload_file('./017/' + filename)
        # clear the container
        # очистите контейнер 
        # (переменная достура к свойствам класса RootWidget в файле root.kv)
        self.root.container.clear_widgets()
        # load the content of the .kv file
        # загрузить содержимое файла .kv
        info = Builder.load_file('./017/' + filename)
        # add the content of the .kv file to the container
        # добавьте содержимое файла .kv в контейнер
        self.root.container.add_widget(info)
# *****************************************************************************************
# если программа не модуль, то выполнить
if __name__ == '__main__':
    # запускаем приложение
    Programm().run()
# *****************************************************************************************