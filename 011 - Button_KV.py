# импорт основного окна App
from kivy.app import App
# импорт модуля Кнопка
from kivy.uix.button import Button
# импорт модуля Строитель - загружает .kv файлы в проект
from kivy.lang import Builder
# загрузить каждый файл .kv по отдельности
Builder.load_file('./011/buttons.kv')

# глобальная переменная счетчик
cnt = int()

class MyButton(Button):
    # метод - нажатие кнопки
    def on_press_button(self):
        # инкремируем счетчик
        global cnt
        cnt += 1
        # показать сообщение на кнопке
        self.text = f'Вы нажали кнопку {cnt} раз !'
        # показать сообщение в stdout
        print(f'Вы нажали кнопку {cnt} раз !')

# создаем основное окно программы, наследуя App - основные свойства окна
class MainApp(App):
    # заголовок окна
    title = 'Button Class'
    # создаем стандартный конструктор Kivy: build(self)
    # где переопределяем некоторые стандартные свойства окна
    def build(self):
        # заголовок окна определяемый в конструкторе
        self.title = 'Button'
        # встраиваем в основное окно объект Кнопка
        return MyButton()

# если программа не модуль, то выполнить
if __name__ == '__main__':
    # запускаем приложение
    MainApp().run()