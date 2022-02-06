# импорт основного окна App
from kivy.app import App
# импорт основного кнопки Button
from kivy.uix.button import Button

# наследуем окно App
class TestApp(App):
    # создаем стандартный конструктор Kivy: build(self)
    def build(self):
        # возвращаем в основное окно App кнопку Button с надписью 'Hello World'
        return Button(text='Hello World')

# запускаем конструктор Kivy на выполнение с помощью метода Kivy: run()
TestApp().run()