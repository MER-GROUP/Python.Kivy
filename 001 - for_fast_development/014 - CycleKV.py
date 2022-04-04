# импорт основного окна App
from kivy.app import App
# импорт модуля Строитель - загружает .kv файлы в проект или строки
from kivy.lang import Builder

# определение строк
KV = '''
#: import Label kivy.uix.label.Label

GridLayout:
    cols: 1
    on_kv_post:
        [self.add_widget(Label(text="Label " + str(i))) for i in range(9)]

'''

# создаем основное окно программы, наследуя App - основные свойства окна
class TestApp(App):
    def build(self):
        # вернуть строки и выполнить
        return Builder.load_string(KV)

# если программа не модуль, то выполнить
if __name__ == '__main__':
    # запускаем приложение
    TestApp().run()