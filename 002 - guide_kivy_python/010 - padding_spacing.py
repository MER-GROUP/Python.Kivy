# *****************************************************************************************
# Отступы.
# Расстояние между элементами
# padding - внутренние отступы. 
# Принимает в качетсве значения список из четырех параметров(отступ сверху,слева,сниху,справа). 
# Например padding = [10,20,10,20].
# spacing - расстояние между элементами. 
# Принимает в качестве значения список из двух параметров. 
# Это расстояние по горизонтали и по вертикали. 
# Например spacing = [10,20].

# Создадим макет Grid Layout(располагает элементы в виде сетки) , где расположим девять кнопок:
# *****************************************************************************************
# главное окно программы
from kivy.app import App
# сеточный макет
from kivy.uix.gridlayout import GridLayout
# кнопка
from kivy.uix.button import Button
# *****************************************************************************************
# окно программы
class ExampleApp(App):
    def build(self):
        #Устанавливаем отсутпы по 10 пикселей с каждой стороны
        # расстояние между элементами по горизонтали 20 пискелей, а по вертикали 30
        gl = GridLayout(cols=3, padding=[10, 10, 10, 10], spacing=[20, 30])
        btn1 = Button(text='Кнопка 1')
        btn2 = Button(text='Кнопка 2')
        btn3 = Button(text='Кнопка 3')
        btn4 = Button(text='Кнопка 4')
        btn5 = Button(text='Кнопка 5')
        btn6 = Button(text='Кнопка 6')
        btn7 = Button(text='Кнопка 7')
        btn8 = Button(text='Кнопка 8')
        btn9 = Button(text='Кнопка 9')
        gl.add_widget(btn1)
        gl.add_widget(btn2)
        gl.add_widget(btn3)
        gl.add_widget(btn4)
        gl.add_widget(btn5)
        gl.add_widget(btn6)
        gl.add_widget(btn7)
        gl.add_widget(btn8)
        gl.add_widget(btn9)
        return gl
# *****************************************************************************************
# запуск программы
# Как мы видим по картинке элементы внутри макета Grid Layout сдвинулись на 10 пикселей 
# со всех сторон и появилось расстояние между элементами по горизонтали на 20 пикселей, 
# а по вертикали на 30 пикселей.
if __name__ == '__main__':
    ExampleApp().run()
# *****************************************************************************************