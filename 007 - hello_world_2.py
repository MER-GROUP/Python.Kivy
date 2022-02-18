# импорт основного окна App
from kivy.app import App
# импорт Текстовой Метки
from kivy.uix.label import Label

# создаем основное окно программы, наследуя App - основные свойства окна
class MainApp(App):
    # создаем стандартный конструктор Kivy: build(self)
    # где переопределяем некоторые стандартные свойства окна
    def build(self):
        # заголовок окна
        self.title = 'Hello world 2'
        # объект с настройками для Label()
        # size_hint - размер текстовой метки
        # pos_hint - положение текстовой метки
        label = Label(text='Hello from Kivy',
                        size_hint=(.5, .5),
                        pos_hint={'center_x': .5, 'center_y': .5})
        # встраиваем в основное окно объект текстовой метки
        return label

# если программа не модуль, то выполнить
if __name__ == '__main__':
    # запускаем приложение
    MainApp().run()