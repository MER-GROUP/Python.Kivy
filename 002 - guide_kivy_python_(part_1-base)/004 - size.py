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
        # Присваим size_hint значение None или 0.Сам size_hint 
        # принимает кортеж (ширину и длину)
        # от 0 до 1.Например если нам нужно чтобы элемент 
        # занимал 10% макета,то нужно поставить значение 0.1
        # Далее в атрибут size который тоже принимает кортеж 
        # устанавливаем в пикселях ширину и длину
        # Обязательно чтобы установить фиксированный 
        # размер элементу, нужно size_hint присвоить None или 0
        btn = Button(text='ok', size_hint=(None, None), size=(150, 150))
        bl.add_widget(btn)
        return bl
# *****************************************************************************************
# запуск программы
# Запускаем приложение и видим что кнопка в нижнем левом углу. 
# Размер кнопки составляет заданным нами 150 пикселей по ширине и высоте:
if __name__ == '__main__':
    TestApp().run()
# *****************************************************************************************