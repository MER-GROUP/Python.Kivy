# *****************************************************************************************
# FileChooser
# Модуль: kivy.uix.filechooser

# FileChooser - файловый менеджер
# FileChooserOpenSave - модальные окна для открытия и сохрания файлов
# *****************************************************************************************
# главное окно программы
from kivy.app import App
# Плавающий макет
from kivy.uix.floatlayout import FloatLayout
# Регистрация и использование объектов
from kivy.factory import Factory
# Свойства объектов
from kivy.properties import ObjectProperty
# Модальные всплывающие окна
from kivy.uix.popup import Popup

# Коробочный макет
from kivy.uix.boxlayout import BoxLayout
# кнопка
from kivy.uix.button import Button
# окно выбора файлов
from kivy.uix.filechooser import FileChooser

# Работа с файлами и директориями
import os
# *****************************************************************************************
# Окно - загрузить файл
class LoadDialog(FloatLayout):
    # ---------------------------------------------------------------------------
    # vars - ObjectProperty
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)
    # ---------------------------------------------------------------------------
# *****************************************************************************************
# Окно - сохранить файл
class SaveDialog(FloatLayout):
    # ---------------------------------------------------------------------------
    # vars - ObjectProperty
    save = ObjectProperty(None)
    text_input = ObjectProperty(None)
    cancel = ObjectProperty(None)
    # ---------------------------------------------------------------------------
# *****************************************************************************************
# Дизайн окна программы
class Root(FloatLayout):
    # ---------------------------------------------------------------------------
    """
    root widget
    """
    # ---------------------------------------------------------------------------
    # vars - ObjectProperty
    # loadfile = ObjectProperty(None)
    # savefile = ObjectProperty(None)
    text_input = ObjectProperty(None)
    # ---------------------------------------------------------------------------
    # закрыть модальное окно
    def dismiss_popup(self):
        self._popup.dismiss()
    # ---------------------------------------------------------------------------
    # показать окно для загрузки файлов
    def show_load(self):
        # объект для модального окна (действия окна)
        content = LoadDialog(load=self.load, cancel=self.dismiss_popup)
        # создаем модальное окно
        self._popup = Popup(title="Load file", content=content,
                            size_hint=(0.9, 0.9))
        # открываем модальное окно
        self._popup.open()
    # ---------------------------------------------------------------------------
    # показать окно для загрузки файлов
    def show_save(self):
        # объект для модального окна (действия окна)
        content = SaveDialog(save=self.save, cancel=self.dismiss_popup)
        # создаем модальное окно
        self._popup = Popup(title="Save file", content=content,
                            size_hint=(0.9, 0.9))
        # открываем модальное окно
        self._popup.open()
    # ---------------------------------------------------------------------------
    # действие кнопки - загрузить файл (Load file)
    def load(self, path, filename):
        with open(os.path.join(path, filename[0])) as stream:
            self.text_input.text = stream.read()
        # закрыть модальное окно
        self.dismiss_popup()
    # ---------------------------------------------------------------------------
    # действие кнопки - сохранить файл (Save file)
    def save(self, path, filename):
        with open(os.path.join(path, filename), 'w') as stream:
            stream.write(self.text_input.text)
        # закрыть модальное окно
        self.dismiss_popup()
    # ---------------------------------------------------------------------------
    pass
# *****************************************************************************************
# окно программы
class Editor(App):
    # ---------------------------------------------------------------------------
    """
    app widget
    """
    # ---------------------------------------------------------------------------
    # def build(self):
    #     return Root()
    # """
    # kv file должет выглядеть так:
    # <Root>:
    #     code 
    #     ...
    #     code
    # """
    # ---------------------------------------------------------------------------
    pass
# *****************************************************************************************
# # регистрация классов в фабрике
# Factory.register('Root', cls=Root)
# Factory.register('LoadDialog', cls=LoadDialog)
# Factory.register('SaveDialog', cls=SaveDialog)
# *****************************************************************************************
# запуск программы
if __name__ == '__main__':
    Editor().run()
# *****************************************************************************************