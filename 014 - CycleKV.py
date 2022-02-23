from kivy.app import App
from kivy.lang import Builder

KV = '''
#: import Label kivy.uix.label.Label

GridLayout:
    cols: 1
    on_kv_post:
        [self.add_widget(Label(text="Label " + str(i))) for i in range(9)]

'''

class TestApp(App):
    def build(self):
        return Builder.load_string(KV)

if __name__ == '__main__':
    TestApp().run()