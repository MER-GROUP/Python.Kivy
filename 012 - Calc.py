# *****************************************************************************************
# импорт основного окна App
from cgitb import text
from kivy.app import App
# импорт модуля Коробочный макет
# в него будем пихать кнопки и др. GUI элементы
from kivy.uix.boxlayout import BoxLayout
# импорт модуля Кнопка
from kivy.uix.button import Button
# импорт модуля Ввод Текста
from kivy.uix.textinput import TextInput
# *****************************************************************************************
# создаем основное окно программы, наследуя App - основные свойства окна
class MainApp(App):
    # создаем стандартный конструктор Kivy: build(self)
    # где переопределяем некоторые стандартные свойства окна
    def build(self):
        # заголовок окна
        self.title = 'Калькулятор'
        # массив операторов
        self.operators = ['/', '*', '+', '-']
        # двумерный массив с наименованиями кнопок
        self.buttons = [['7', '8', '9', '/'],
                        ['4', '5', '6', '*'],
                        ['1', '2', '3', '-'],
                        ['.', '0', 'C', '+']]
        # был ли нажат последней кнопкой оператор (False/True)
        self.last_was_operator = None
        # какой была последняя кнопка
        self.last_button = None

        # создаем основной коробочный макет
        # orientation='vertical' - вертикальная ориентация
        main_layout = BoxLayout(orientation='vertical')

        # создаем поле для ввода текста
        # multiline=False - в текстовом поле только одна линия для ввода
        # readonly=True - текстовое поле только для чтения, но не для ввода
        # halign='right' - горизонтальное выравнивание текста - вправо
        # font_size=55 - размер шрифта текста
        self.solution = TextInput(multiline=False,
                                    readonly=True,
                                    halign='right',
                                    font_size=55)

        # добавляем поле для ввода текста в коробочный макет
        main_layout.add_widget(self.solution)

        # добавляем кнопки с названиями в коробочный макет
        # создаем доп. коробочный макет куда будем складывать кнопки
        # в цикле создаем кнопки, присваиваем им названия и кладем в доп. коробочный макет
        # в цикле каждую кнопку связываем с методом 
        # доп. коробочный макет кладем в основной коробочный макет
        # text=name - задаем имя кнопки
        # font_size=55 - размер шрифта кнопки
        # pos_hint={'center_x': 0.5, 'center_y': 0.5} - расположение кнопки
        for row_names in self.buttons:
            h_layout = BoxLayout()
            for name in row_names:
                button = Button(text=name, 
                                font_size=55,
                                pos_hint={'center_x': 0.5, 'center_y': 0.5})
                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)
            main_layout.add_widget(h_layout)

        # кнопка =
        # text=name - задаем имя кнопки
        # font_size=55 - размер шрифта кнопки
        # pos_hint={'center_x': 0.5, 'center_y': 0.5} - расположение кнопки
        equils_button = Button(text='=',
                                font_size=55,
                                pos_hint={'center_x': 0.5, 'center_y': 0.5})
        # кнопку связываем с методом
        # equils_button.bind(on_press=self.)
        # кнопку = кладем в основной коробочный макет
        main_layout.add_widget(equils_button)

        # встраиваем в основное окно коробочный макет 
        # где мы расположили кнопки и поле для ввода текста
        return main_layout

    # метод нажатия кнопок 
    # instance - является button самим объектом
    # instance - является копией объекта Button (копией переданного объекта)
    # из button.bind(on_press=self.on_button_press)
    def on_button_press(self, instance):
        # берем значение из поле для ввода текста TextInput
        current = self.solution.text
        # берем значение из нажатой кнопки
        button_text = instance.text

        # если нажата кнопка C
        # то очистить поле для ввода текста TextInput
        if 'C' == button_text:
            self.solution.text = ''
        else:
            pass
# *****************************************************************************************
# если программа не модуль, то выполнить
if __name__ == '__main__':
    # запускаем приложение
    MainApp().run()
# *****************************************************************************************