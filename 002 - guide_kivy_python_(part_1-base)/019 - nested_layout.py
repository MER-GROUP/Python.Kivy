# *****************************************************************************************
# Вложенные макеты
# Любой макет можно вложить в другой макет. 
# Давайте напишем небольшое приложение, 
# где создадим три макета: Page Layout, Box Layout и Stack Layout. 
# В Box Layout и Stack layout добавим по четыре кнопки. 
# Далее добавим в Page Layout макеты Box Layout и Stack Layout:
# *****************************************************************************************
# главное окно программы
from kivy.app import App
# стэковый макет
from kivy.uix.stacklayout import StackLayout
# коробочный макет
from kivy.uix.boxlayout import BoxLayout
# страничный макет
from kivy.uix.pagelayout import PageLayout
# кнопка
from kivy.uix.button import Button
# *****************************************************************************************
# окно программы
class NestedLayoutsApp(App):
    # ---------------------------------------------------------------------------
    def build(self):
        pl = PageLayout()

        bl = BoxLayout(orientation='vertical')
        btn1 = Button(text='Кнопка 1')
        btn2 = Button(text='Кнопка 2')
        btn3 = Button(text='Кнопка 3')
        btn4 = Button(text='Кнопка 4')
        bl.add_widget(btn1)
        bl.add_widget(btn2)
        bl.add_widget(btn3)
        bl.add_widget(btn4)

        sl = StackLayout(orientation='lr-bt')
        btn5 = Button(text='Кнопка 5', size_hint=(0.25, 0.5))
        btn6 = Button(text='Кнопка 6', size_hint=(0.25, 0.5))
        btn7 = Button(text='Кнопка 7', size_hint=(0.25, 0.5))
        btn8 = Button(text='Кнопка 8', size_hint=(0.25, 0.5))
        sl.add_widget(btn5)
        sl.add_widget(btn6)
        sl.add_widget(btn7)
        sl.add_widget(btn8)

        pl.add_widget(bl)
        pl.add_widget(sl)

        return pl
    # ---------------------------------------------------------------------------
# *****************************************************************************************
# запуск программы
if __name__ == '__main__':
    NestedLayoutsApp().run()
# *****************************************************************************************