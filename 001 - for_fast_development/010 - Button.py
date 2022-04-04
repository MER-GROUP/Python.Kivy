# импорт основного окна App
from kivy.app import App
# импорт модуля Кнопка
from kivy.uix.button import Button

# глобальная переменная счетчик
cnt = int()

# создаем основное окно программы, наследуя App - основные свойства окна
class MainApp(App):
    # создаем стандартный конструктор Kivy: build(self)
    # где переопределяем некоторые стандартные свойства окна
    def build(self):
        # заголовок окна
        self.title = 'Button'
        # объект с настройками для Button()
        # size_hint - размер текстовой метки
        # pos_hint - положение текстовой метки
        button = Button(text='Hello from Kivy',
                        size_hint=(.5, .5),
                        pos_hint={'center_x': .5, 'center_y': .5})
        # выполнить действие если кнопку нажали
        # bind - связывает событие с методом объекта
        # on_press - событие (если кнопка нажата)
        # on_press_button - метод объекта (класса)
        button.bind(on_press=self.on_press_button)
        # встраиваем в основное окно объект Кнопка
        return button

    # метод - нажатие кнопки
    # instance - является button самим объектом
    def on_press_button(self, instance):
        # инкремируем счетчик
        global cnt
        cnt += 1
        # показать сообщение в заголовке окна
        self.title = f'Вы нажали кнопку {cnt} раз !'
        # показать сообщение в stdout
        print(f'Вы нажали кнопку {cnt} раз !')

# если программа не модуль, то выполнить
if __name__ == '__main__':
    # запускаем приложение
    MainApp().run()