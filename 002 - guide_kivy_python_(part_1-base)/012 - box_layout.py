# *****************************************************************************************
# Box Layout
# Модуль: kivy.uix.boxlayout

# Box Layout - это макет в которым виджеты располагаются последовательно, 
# в «вертикальной» или «горизонтальной» ориентации.

# Атрибуты
# orientation - принимает значение "horizontal"(виждеты будут расположены по горизонтали) 
# или "vertical"(виджеты будут расположены по вертикали).
# spacing - расстояние между виджетами внутри макета в пикселях. По умолчанию 0.
# padding - внутренние отступы. Принимает список значений 
# в пискелях "[padding_left, padding_top, padding_right, padding_bottom]".
# Так же можно назначить отступ по горизонтали и 
# вертикали "[padding_horizontal, padding_vertical]" или одинаковое значение 
# отступов со всех сторон "[padding]".

# Методы
# add_widget(widget) - добавляет виджет в макет.
# remove_widget(widget) - удаляет виджет с макета.

# Пример
# Создадим макет Box Layout, в котором расположим две кнопки последовательно по вертикали 
# и зададим расстояние между ними в 10 пикселей, а также отступы co всех сторон 
# от макета в 20 пикселей:
# *****************************************************************************************
# главное окно программы
from kivy.app import App
# коробочный макет
from kivy.uix.boxlayout import BoxLayout
# кнопка
from kivy.uix.button import Button
# *****************************************************************************************
# окно программы
class BoxLayoutApp(App):
    # ---------------------------------------------------------------------------
    def build(self):
        # вертикальная ориентация
        bl = BoxLayout(orientation='vertical', padding=20, spacing=10)
        # горизонтальная ориентация
        # bl = BoxLayout(orientation='horizontal', padding=20, spacing=10)
        # тоже верно
        # bl = BoxLayout(orientation='vertical', padding=[20], spacing=10)
        btn1 = Button(text='Кнопка 1')
        btn2 = Button(text='Кнопка 2')
        bl.add_widget(btn1)
        bl.add_widget(btn2)
        return bl
    # ---------------------------------------------------------------------------
# *****************************************************************************************
# запуск программы
if __name__ == '__main__':
    BoxLayoutApp().run()
# *****************************************************************************************