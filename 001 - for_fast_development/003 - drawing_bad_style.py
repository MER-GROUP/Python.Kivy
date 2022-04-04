# пример рисования - плохой стиль
# импорт основного окна App
from kivy.app import App
# импорт основного окна для рисования Widget
from kivy.uix.widget import Widget
# импорт графических инструментов
from kivy.graphics import *

# Создаем класс для рисования наследуя Widget
class My2Widget(Widget):
    # конструктор
    def __init__(self, **kwargs):
        # вызываем конструктор из класса родителя
        # super(My2Widget, self).__init__(**kwargs)
        super().__init__(**kwargs)
        # делаем обновление холста по позиции и размеру
        self.bind(pos=self.update_canvas)
        self.bind(size=self.update_canvas)
        # вызываем метод update_canvas - обновить холст
        self.update_canvas()

    # метод обновления холста
    def update_canvas(self, *args):
        # очищвем холст
        self.canvas.clear()
        # задаем свойства холста
        with self.canvas:
            # задаем цвет фигуры-объекта
            Color(0.5, 0.5, 0.5, 0.5)
            # задаем фигуру
            Ellipse(pos=self.pos, size=self.size)

# Создаем класс основного окна программы и наследуем основное окно программы App
class MyApp(App):
    # создаем стандартный конструктор Kivy: build(self)
    def build(self):
        # возвращаем в основное окно App окно для рисования Widget
        return My2Widget()

if __name__ =='__main__':
    MyApp().run()