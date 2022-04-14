# *****************************************************************************************
# Page Layout
# Модуль: kivy.uix.pagelayout

# Page Layout - это макет, в котором каждый добавленный виджет 
# будет являться отдельной страницей. Потянув за правый край 
# влево можно переключиться на следующую страницу и так же потянув 
# за левый край вправо можно переключиться на предыдущую страницу. 
# Забегая вперед скажу, что каждый макет можно добавлять в другой макет.
# Так и в Page Layout можно добавить другие макеты и перелистывать их.

# Атрибуты
# anim_kwargs - принимает в качестве значения словарь. 
    # С помощью этого атрибута можно изменять анимацию перелистывания. 
    # По умолчанию "{'d': .5, 't': 'in_quad'}".
# border - ширина границы вокруг текущей страницы, 
    # используемая для отображения областей прокрутки 
    # предыдущей / следующей страницы при необходимости.
# page - принимает номер текущей отображаемой старницы по умолчанию.
# swipe_threshold - пороговое значение используется для запуска 
    # пролистывания в процентах от размера виджета. 
    # Принимает значения от 0 до 1. По умолчанию 0.5.

# Методы
# add_widget(widget) - добавляет виджет в макет.
# remove_widget(widget) - удаляет виджет с макета.

# Пример
# Создадим Page Layout и три кнопки, где каждая кнопка будет отельной страницей:
# *****************************************************************************************
# главное окно программы
from kivy.app import App
# страничный макет
from kivy.uix.pagelayout import PageLayout
# кнопка
from kivy.uix.button import Button
# *****************************************************************************************
# окно программы
class PageLayoutApp(App):
    # ---------------------------------------------------------------------------
    def build(self):
        pl = PageLayout()
        btn1 = Button(text='Кнопка 1')
        btn2 = Button(text='Кнопка 2')
        btn3 = Button(text='Кнопка 3')
        pl.add_widget(btn1)
        pl.add_widget(btn2)
        pl.add_widget(btn3)
        return pl
    # ---------------------------------------------------------------------------
# *****************************************************************************************
# запуск программы
if __name__ == '__main__':
    PageLayoutApp().run()
# *****************************************************************************************