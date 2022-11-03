# *****************************************************************************************
# FileChooser
# Модуль: kivy.uix.filechooser

# FileChooser - файловый менеджер
# *****************************************************************************************
# главное окно программы
from kivy.app import App
# Коробочный макет
from kivy.uix.boxlayout import BoxLayout
# кнопка
from kivy.uix.button import Button
# окно выбора файлов
from kivy.uix.filechooser import FileChooser

# *****************************************************************************************
# Дизайн окна программы
class MainWindow(BoxLayout):
    # ---------------------------------------------------------------------------
    """
    app widget
    """
    # ---------------------------------------------------------------------------
    pass
# *****************************************************************************************
# окно программы
class FileChooserApp(App):
    # ---------------------------------------------------------------------------
    """
    root widget
    """
    # ---------------------------------------------------------------------------
    def build(self):
        return MainWindow()
    # ---------------------------------------------------------------------------
    pass
    # ---------------------------------------------------------------------------
# *****************************************************************************************
# запуск программы
if __name__ == '__main__':
    FileChooserApp().run()
# *****************************************************************************************