# *****************************************************************************************
# DropDown
# Модуль: kivy.uix.dropdown

# DropDown - выпадающее меню из кнопок
# *****************************************************************************************
# главное окно программы
from kivy.app import App
# выпадающее меню из кнопок
from kivy.uix.dropdown import DropDown
# кнопка
from kivy.uix.button import Button
# base
from kivy.base import runTouchApp
# *****************************************************************************************
# окно программы
class DropDownApp(App):
    # ---------------------------------------------------------------------------
    def build(self):
        # созжаем меню DropDown и заполняем его кнопками (Button)
        dropdown = DropDown()
        for index in range(10):
            btn = Button(text='Value %d' % index, size_hint_y=None, height=44)
            btn.bind(on_release=lambda btn: dropdown.select(btn.text))
            dropdown.add_widget(btn)

        # создаем кнопку где будет находиться выпадающее меню DropDown
        mainbutton = Button(text='Hello', size_hint=(None, None))
        # при нажатии на кнопку открываем выпадающее меню DropDown
        mainbutton.bind(on_release=dropdown.open)

        # при нажатии на кнопку из выпадающего меню DropDown 
        # меняем название (текст) кнопки mainbutton которая хранит выпадающее меню DropDown
        dropdown.bind(on_select=lambda instance, x: setattr(mainbutton, 'text', x))

        # связываем mainbutton и dropdown 
        # и возвращаем готовый объект-виджет
        return runTouchApp(mainbutton)
    # ---------------------------------------------------------------------------
    pass
    # ---------------------------------------------------------------------------
# *****************************************************************************************
# запуск программы
if __name__ == '__main__':
    DropDownApp().run()
# *****************************************************************************************