# импорт основного окна App
from distutils.log import info
from kivy.app import App
# импортируем модуль Свойство Объекта
# модуль дает доступ к переменным и свойствам KV файлов
from kivy.properties import ObjectProperty, StringProperty
# импорт модуля Плавающий макет
# в него будем пихать кнопки и др. GUI элементы
from kivy.uix.floatlayout import FloatLayout
# импорт модуля Строитель - загружает .kv файлы в проект
from kivy.lang import Builder
# закрузить файл
Builder.load_file('./016/Controller.kv')

# создаем основное окно программы, наследуя App - основные свойства окна
class ControllerApp(App):
    def build(self):
        # встраиваем в основное окно объект Плавающий макет
        # дизайн и функционал основного окна
        # info - общая переменная класса class Controller(FloatLayout)
        # и файла Controller.kv созданная объектом StringProperty()
        # StringProperty() - записывает переменные 
        # в конструктор класса class Controller(FloatLayout)
        return Controller(info='Hello World')

# создаем основной плавающий макет
# описание свойств класса - ./016/Controller.kv
class Controller(FloatLayout):
    # получаем доступ к объекту (свойству или параметру) в файле Controller.kv
    label_wid = ObjectProperty()
    # делаем общую текстовую переменную для класса class Controller(FloatLayout) 
    # и файла Controller.kv 
    info = StringProperty()
    # метод
    # если нажать на кнопуц 
    # то изменить надписи на кнопке и этикетке
    # метод связываем с нажатием кнопки в файле Controller.kv
    def do_action(self):
        # изменим надпись на кнопке
        self.info = 'New info text'
        # изменим надпись на этикетке
        self.label_wid.text = 'My label after button press'

# если программа не модуль, то выполнить
if __name__ == '__main__':
    # запускаем приложение
    ControllerApp().run()