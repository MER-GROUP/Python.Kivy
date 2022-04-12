# *****************************************************************************************
# импорт основного окна App
from kivy.app import App
# импорт располодения сетки
from kivy.uix.gridlayout import GridLayout
# импорт кнопок в проект
from kivy.uix.button import Button
# импортируем модуль Свойство Объекта
from kivy.properties import ObjectProperty
# импорт модуля Строитель - загружает .kv файлы в проект
from kivy.lang import Builder
'''
# загрузить каждый файл .kv по отдельности
# Описываем класс MainApp
Builder.load_file('./006/main.kv')
# Описываем класс AddButton, SubtractButton
Builder.load_file('./006/buttons.kv')
'''
# listdir - показывает файлы в конкретной папке
from os import listdir
# записываем директорию в переменную kv_path
kv_path = './006/'
# загрузить все файлы .kv по отдельности
for kv in listdir(kv_path):
    Builder.load_file(kv_path + kv)
# *****************************************************************************************
# создаем свой контейнер, где будем хранить унаследованную сетку
class Container(GridLayout):
    # описание класса в container.kv
    # определяем переменную display со свойством ObjectProperty()
    display = ObjectProperty()
    # метод добавления
    def add_one(self):
        # присваиваем значение переменной из container.kv -> Label -> text
        # конвертируем в целое число
        value = int(self.display.text)
        # инкрементируем значение переменной text на 1
        # и присваиваем значение переменной в container.kv -> Label -> text
        self.display.text = str(value + 1)
    # метод вычитания
    def subtract_one(self):
        # присваиваем значение переменной из container.kv -> Label -> text
        # конвертируем в целое число
        value = int(self.display.text)
        # декрементируем значение переменной text на 1
        # и присваиваем значение переменной в container.kv -> Label -> text
        self.display.text = str(value - 1)
# *****************************************************************************************
# класс добавить кнопку, наследует кнопку
class AddButton(Button):
    # описание класса в buttons.kv
    pass
# *****************************************************************************************
# класс вычесть кнопку, наследует кнопку
class SubtractButton(Button):
    # описание класса в buttons.kv
    pass
# *****************************************************************************************
# создаем основное окно программы, наследуя App - основные свойства окна
class MainApp(App):
    # создаем стандартный конструктор Kivy: build(self)
    # где переопределяем некоторые стандартные свойства окна
    def build(self):
        # заголовок окна
        self.title = 'Это заголовок окна !'
        # встраиваем в основное окно наш созданный контейнер, 
        # где мы храним сетку
        return Container()
# *****************************************************************************************
# если программа не модуль, то выполнить
if __name__ == '__main__':
    # создаем объект приложения
    app = MainApp()
    # запускаем приложение
    app.run()
# *****************************************************************************************