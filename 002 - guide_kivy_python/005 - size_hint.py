# *****************************************************************************************
# Размеры и позиционирование
# Размеры
# Для задания размера элемента есть два атрибута size и size_hint. 
# По умолчанию используется size_hint, который принимает значения 
# ширины и длины от 0(0% макета) до 1(100% макета). Если значение 
# установлено в 1, то элемент растягивается на весь макет.
# Если 0 (так же можно установить значения "None"), то элемент 
# не привязывается к размеру макета и тем самым можно установить 
# фиксированное значение элемента с помошью атрибута size в пикселях. 
# Например:
# *****************************************************************************************
# главное окно программы
from kivy.app import App
# коробочный макет
from kivy.uix.boxlayout import BoxLayout
# кнопка
from kivy.uix.button import Button
# *****************************************************************************************
# окно программы
class TestApp(App):
    def build(self):
        bl = BoxLayout()
        # Давайте назначим кнопке 30% размера от макета и посмотрим что получится:
        btn = Button(text='ok', size_hint=(0.3, 0.3))
        bl.add_widget(btn)
        return bl
# *****************************************************************************************
# запуск программы
# Как мы видим кнопка заняла по ширине 100%(хотя указали 30%), а по длине 30%. 
# Все потому что мы используем макет Box Layout, 
# который распологает элементы по горизонтали или вертикали. 
# По умолчанию Box Layout распологает элементы по горизонтали 
# и так как в нем одна только кнопка, то он растягивает её на всё ширину. 
if __name__ == '__main__':
    TestApp().run()
# *****************************************************************************************