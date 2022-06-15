# *****************************************************************************************
# CheckBox
# Модуль: kivy.uix.checkbox

# CheckBox - кнопка которая может быть либо отмечена, либо не отмечена.

# Атрибуты
# active - указывает, является ли CheckBox активным или нет. 
    # Принимает в качестве значения "True" или "False".
# on_press - событие при нажатие на кнопку. 
    # Принимает в качестве значения названия метода.

# Методы
# bind(событие = название метода) - с помощью метода bind можно привязать к событию метод.

# Пример
# Создадим приложение где при нажатии на CheckBox, 
# если поставлена галочка в Label будет выводиться "CheckBox активен", 
# а если нет то "CheckBox не активен:"
# *****************************************************************************************
# главное окно программы
from kivy.app import App
# коробочный макет
from kivy.uix.boxlayout import BoxLayout
# кнопка флажок
from kivy.uix.checkbox import CheckBox
# текст (этикетка)
from kivy.uix.label import Label
# *****************************************************************************************
# окно программы
class CheckBoxApp(App):
    # ---------------------------------------------------------------------------
    def build(self):
        self.bl = BoxLayout(orientation='horizontal', pos_hint={'center_x': 0.8, 'center_y': 1.0})
        self.checkbox = CheckBox(size_hint=(None, None))
        self.label = Label(text='CheckBox не активен', size_hint=(None, None))
        self.checkbox.bind(on_press=self.on_checkbox_active)
        self.bl.add_widget(self.checkbox)
        self.bl.add_widget(self.label)
        return self.bl
    # ---------------------------------------------------------------------------
    def on_checkbox_active(self, value):
        if self.checkbox.active:
            self.label.text = 'CheckBox активен'
        else:
            self.label.text = 'CheckBox не активен'
    # ---------------------------------------------------------------------------
# *****************************************************************************************
# запуск программы
if __name__ == '__main__':
    CheckBoxApp().run()
# *****************************************************************************************