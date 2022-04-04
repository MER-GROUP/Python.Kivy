# пример рисования - хороший стиль
# импорт основного окна App
from kivy.app import App
# импорт основного окна для рисования Widget
from kivy.uix.widget import Widget

# Создаем класс для рисования наследуя Widget
class MyWidget(Widget):
    pass

# Создаем класс основного окна программы и наследуем основное окно программы App
class MyApp(App):
    # создаем стандартный конструктор Kivy: build(self)
    def build(self):
        # возвращаем в основное окно App окно для рисования Widget
        return MyWidget()

# если программа не модуль то выполнить программу
if __name__ =="__main__":
    # запускаем конструктор Kivy на выполнение с помощью метода Kivy: run()
    MyApp().run()