# *****************************************************************************************
# Scatter Layout
# Модуль: kivy.uix.scatterlayout

# Scatter Layout - этот макет похож на Relative Layout. 
    # Отличается этот макет тем, что его можно перемещать вместе с виджетами, 
    # масштабировать и вращать. Чтобы перетащить данный макет нужно зажать 
    # на свободной области левой кнопкой мышки и перетаскивать. 
    # Чтобы вращать нужно на правую кнопку мышки поставить красную точку 
    # и на макете на пустой области зажать левой кнопкой мышки и вращать мышкой. 
    # Для маштабирования так же надо поставить красную точку зажать левой кнопкой 
    # мыши на пустой области макета и двигать мышкой вверх или вниз. 
    # Для того чтобы убрать красную точку надо нажать на неё два раза. 
    # Так же такое же поведение макета можно сделать и в Float Layout для этого 
    # нужно экспортировать виджет scatter из пакета kivy.uix.scatter и добавить 
    # его во Float Layout, а уже другие виджеты в scatter.

# Методы
# add_widget(widget) - добавляет виджет в макет.
# remove_widget(widget) - удаляет виджет с макета.
# clear_widgets() - удаляет все или добавленный в параметры список виджетов.

# Пример
# Создадим Scatter Layout и добавим в него Label(текст). 
# Далее переместим макет с Label в центр, 
# увеличим маштаб и перевернем макет с Label:
# *****************************************************************************************
# главное окно программы
from kivy.app import App
# разбросанный макет
from kivy.uix.scatterlayout import ScatterLayout
# текст (этикетка)
from kivy.uix.label import Label
# *****************************************************************************************
# окно программы
class ScatterLayoutApp(App):
    # ---------------------------------------------------------------------------
    def build(self):
        sl = ScatterLayout()
        #Устнавливаем ширину текста в 20%, а высоту в 10% size_hint = (0.2,0.1)
        # lb = Label(text='Текст 1', size_hint = (0.2 ,0.1 ))
        lb = Label(text='Текст 1')
        sl.add_widget(lb)
        return sl
    # ---------------------------------------------------------------------------
# *****************************************************************************************
# запуск программы
if __name__ == '__main__':
    # Перемещаем макет с Label. Зажимаем левой клавишой мыши и перетаскиваем на 
    # пустую область макета.
    # Увеличим маштаб Label. Для этого ставим красную точку на правую кнопку 
    # мыши и на пустой области зажимаем левой кнопкой мыши и двигаем мышкой вверх:
    # Теперь перевернем Label. Для этого так же на пустой области макета зажимаем 
    # левой кнопкой мыши и вращаем мышкой.
    # Чтобы теперь убрать красную точку нажимаем на неё два раза левой кнопкой мыши.
    ScatterLayoutApp().run()
# *****************************************************************************************