# *****************************************************************************************
# Accordion
# Модуль: kivy.uix.accordion

# Accordion - представляет собой форму меню, 
# в котором параметры располагаются вертикально или горизонтально, 
# а при нажатии на элемент открывается для отображения его содержимое.
# Accordion состоит из элементов AccordionItem. В AccordionItem можно помещать, 
# как виджеты, так и макеты.

# Структура
# Accordion:
#     AccordionItem:
#         Контент(виджеты или макеты)
#     AccordionItem:
#         BoxLayout(макет):
#                 Контент(виджеты или макеты)

# Атрибуты
# orientation - принимает значение "horizontal"(горизонтальное расположение элементов) 
# или "vertical"(вертикальное расположение элементов).
# anim_duration - продолжительность анимации в секундах при выборе нового элемента аккордеона. 
# По умолчанию 0.25 (250мс).
# min_space - минимальное пространство для заголовка каждого элемента. 
# Это значение автоматически устанавливается для каждого дочернего элемента каждый раз, 
# когда происходит событие макета. По умолчанию 44 px.

# Методы
# add_widget(AccordionItem) - добавляет элемент Accordion Item.
# remove_widget(AccordionItem) - удаляет элемент Accordion Item.

# AccordionItem
# Модуль: kivy.uix.accordion

# Атрибуты
# title - заголовок элемента меню.

# Методы
# add_widget(Widget) - добавляет виджет или макет.
# remove_widget(Widget) - удаляет виджет или макет.

# Пример
# Создадим Accordion и добавим в него два AccordionItem. 
# Добавим в каждый AccrodionItem макет Box Layout. 
# В один Box Layout поместим три кнопки, а в другой три лейбла:
# *****************************************************************************************
# главное окно программы
from kivy.app import App
# menu Accordion
from kivy.uix.accordion import Accordion, AccordionItem
# коробочный макет
from kivy.uix.boxlayout import BoxLayout
# текст
from kivy.uix.label import Label
# кнопка
from kivy.uix.button import Button
# *****************************************************************************************
# окно программы
class AccordionApp(App):
    # ---------------------------------------------------------------------------
    def build(self):
        accordion = Accordion(orientation='vertical')

        bl1 = BoxLayout(orientation='vertical')
        btn1 = Button(text='Кнопка 1')
        btn2 = Button(text='Кнопка 2')
        btn3 = Button(text='Кнопка 3')
        bl1.add_widget(btn1)
        bl1.add_widget(btn2)
        bl1.add_widget(btn3)
        accordion_item1 = AccordionItem(title='Кнопки')
        accordion_item1.add_widget(bl1)

        bl2 = BoxLayout(orientation='vertical')
        lb1 = Label(text='Строка 1')
        lb2 = Label(text='Строка 2')
        lb3 = Label(text='Строка 3')
        bl2.add_widget(lb1)
        bl2.add_widget(lb2)
        bl2.add_widget(lb3)
        accordion_item2 = AccordionItem(title='Строки')
        accordion_item2.add_widget(bl2)

        accordion.add_widget(accordion_item1)
        accordion.add_widget(accordion_item2)

        return accordion
    # ---------------------------------------------------------------------------
# *****************************************************************************************
# запуск программы
if __name__ == '__main__':
    AccordionApp().run()
# *****************************************************************************************