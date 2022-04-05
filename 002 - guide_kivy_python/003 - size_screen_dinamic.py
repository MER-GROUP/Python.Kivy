# *****************************************************************************************
# Второй способ это динамически изменить размер 
# после создания окна. Для этого импортируем 
# класс Window из модуля kivy.core.window:
# *****************************************************************************************
# главное окно программы
from kivy.app import App
# коробочный макет
from kivy.uix.boxlayout import BoxLayout
# конфигурация главного окна программы
# from kivy.core.window import Window
from kivy.core.window import Window
# *****************************************************************************************
# размеры главного окна
Window.size = (400, 300)
# *****************************************************************************************
# окно программы
class TestApp(App):
    # ---------------------------------------------------------------------------
    def build(self):
        bl = BoxLayout()
        return bl
    # ---------------------------------------------------------------------------
# *****************************************************************************************
# запуск программы
if __name__ == '__main__':
    TestApp().run()
# *****************************************************************************************
