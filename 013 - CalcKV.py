# *****************************************************************************************
# импорт основного окна App
from kivy.app import App
# импорт модуля Коробочный макет
# в него будем пихать кнопки и др. GUI элементы
from kivy.uix.boxlayout import BoxLayout
# импорт модуля Кнопка
from kivy.uix.button import Button
# импорт модуля Ввод Текста
from kivy.uix.textinput import TextInput
# импортируем модуль Свойство Объекта 
# для работы с KV файлами
# from kivy.properties import ObjectProperty
# импорт модуля os - работа с файлами и папками
# listdir - показывает файлы в конкретной папке
from os import listdir
# импорт модуля Строитель - загружает .kv файлы в проект
from kivy.lang import Builder
# записываем директорию в переменную kv_path
kv_path = './013/'
# загрузить все файлы .kv по отдельности
for kv_file in listdir(kv_path):
    Builder.load_file(kv_path + kv_file)
# *****************************************************************************************
# создаем основное окно программы, наследуя App - основные свойства окна
class Calc(App):
    # создаем стандартный конструктор Kivy: build(self)
    # где переопределяем некоторые стандартные свойства окна
    def build(self):
        # заголовок окна
        self.title = 'Калькулятор'
        # встраиваем в основное окно объект Коробочный макет
        # дизайн и функционал основного окна
        return Maket()
# *****************************************************************************************
# создаем основной коробочный макет
# описание свойств класса - ./013/Maket.kv
class Maket(BoxLayout):
    # определяем переменную solution со свойством ObjectProperty()
    # solution = ObjectProperty()
    # массив операторов
    operators = ['/', '*', '+', '-']
    # двумерный массив с наименованиями кнопок
    buttons = [['7', '8', '9', '/'],
                    ['4', '5', '6', '*'],
                    ['1', '2', '3', '-'],
                    ['.', '0', 'C', '+']]
    # был ли нажат последней кнопкой оператор (False/True)
    last_was_operator = None
    # какой была последняя кнопка
    last_button = None

    # инициализируем поле для ввода текста
    # multiline=False - в текстовом поле только одна линия для ввода
    # readonly=True - текстовое поле только для чтения, но не для ввода
    # halign='right' - горизонтальное выравнивание текста - вправо
    # font_size=55 - размер шрифта текста
    solution = TextInput(multiline=False,
                                    readonly=True,
                                    halign='right',
                                    font_size=55)

    # метод - создает много кнопок
    # проектируем кнопки калькулятора, делаем дизайн
    def buttons_many(self):
        # добавляем кнопки с названиями в коробочный макет
        # создаем коробочный макет куда будем складывать по 4 кнопки в ряд вертикально
        # создаем доп. коробочный макет куда будем складывать кнопки горизонтально
        # в цикле создаем кнопки, присваиваем им названия и кладем в доп. коробочный макет
        # в цикле каждую кнопку связываем с методом 
        # доп. коробочный макет кладем в основной коробочный макет
        # text=name - задаем имя кнопки
        # font_size=55 - размер шрифта кнопки
        # pos_hint={'center_x': 0.5, 'center_y': 0.5} - расположение кнопки
        main_layout = BoxLayoutDecoratorVertical()
        for row_names in self.buttons:
            h_layout = BoxLayoutDecoratorHorizontal()
            for name in row_names:
                button = Buttons(text=name, 
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
        # кнопку связываем с методом - выполнения действия рператоров
        equils_button.bind(on_press=self.on_solution)
        # кнопку = кладем в основной коробочный макет
        main_layout.add_widget(equils_button)

        # возвращаем спроектированные кнопки
        return main_layout

    # метод нажатия кнопок
    # вводятся цифры и операторы действия в поле для ввода текста TextInput
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
            # Не добавлять два оператора сразу друг за другом
            # return - не обновлять деуствие (нажатие кнопки)
            if current and (self.last_was_operator and button_text in self.operators):
                return
            # Первый символ не может быть оператором
            # return - не обновлять деуствие (нажатие кнопки)
            elif '' == current and (button_text in self.operators):
                return
            # иначе обновляем поле для ввода текста TextInput
            else:
                new_text = current + button_text
                self.solution.text = new_text

        # фиксируем последнее нажатие
        self.last_button = button_text
        # определяем было ли последнее нажатие оператором
        self.last_was_operator = self.last_button in self.operators

    # метод выполнения действия рператоров
    # instance - является button самим объектом
    # instance - является копией объекта Button (копией переданного объекта)
    # из button.bind(on_press=self.on_button_press)
    def on_solution(self, instance):
        # берем значения из поле для ввода текста TextInput
        text = self.solution.text
        # если значение не пустое
        # то выполнить действие с указанным оператором
        # и вывести результат в поле для ввода текста TextInput
        # eval - вычисляет текстовое выражение и возвращает результат выражения (no str)
        if text:
            solution = str(eval(self.solution.text))
            self.solution.text = solution
# *****************************************************************************************
# создаем декоратор коробочный макет
# описание свойств класса - ./013/Buttons.kv
class Buttons(Button):
    pass
# *****************************************************************************************
# создаем поле для ввода текста
# описание свойств класса - ./013/Decorator.kv
class BoxLayoutDecoratorVertical(BoxLayout):
    pass
# *****************************************************************************************
# создаем поле для ввода текста
# описание свойств класса - ./013/Decorator.kv
class BoxLayoutDecoratorHorizontal(BoxLayout):
    pass
# *****************************************************************************************
# если программа не модуль, то выполнить
if __name__ == '__main__':
    # запускаем приложение
    Calc().run()
# *****************************************************************************************