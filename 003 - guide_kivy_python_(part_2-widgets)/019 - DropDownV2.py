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
# Коробочный макет
from kivy.uix.boxlayout import BoxLayout
# работа с экраном программы
from kivy.uix.screenmanager import ScreenManager, Screen
# работа со свойствами объекта
from kivy.properties import ObjectProperty, StringProperty
# *****************************************************************************************
# декоратор для DropDown
class CustomDropDown(DropDown):
    pass
# *****************************************************************************************
# декоратор для Screen
# дизайн программы
# class HomeScreen(Screen):
class HomeScreen(BoxLayout):
    # ---------------------------------------------------------------------------
    '''root widget'''
    # ---------------------------------------------------------------------------
    #vars
    pass
    # ---------------------------------------------------------------------------
    # конструктор класса HomeScreen
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.drop_down = CustomDropDown()
    # def __init__(self, *args, **kwargs):
    #     super(HomeScreen, self).__init__(*args, **kwargs)
    #     self.drop_down = CustomDropDown()
    # ---------------------------------------------------------------------------
# *****************************************************************************************
# окно программы
class DropDown2App(App):
    # ---------------------------------------------------------------------------
    '''app widget'''
    # ---------------------------------------------------------------------------
    #vars
    menu_str = StringProperty('MENU')
    # ---------------------------------------------------------------------------
    def build(self):
        # # связываем mainbutton и dropdown 
        # # и возвращаем готовый объект-виджет
        # return runTouchApp(mainbutton)
        return HomeScreen()
    # ---------------------------------------------------------------------------
    pass
    # ---------------------------------------------------------------------------
# *****************************************************************************************
# запуск программы
if __name__ == '__main__':
    DropDown2App().run()
# *****************************************************************************************