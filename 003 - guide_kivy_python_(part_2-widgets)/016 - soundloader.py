from kivy.app import App
from kivy.core.audio import SoundLoader
from kivy.uix.floatlayout import FloatLayout

class MyFloatLayout(FloatLayout):
    def play_music(self):
        music = SoundLoader.load('Nickelback.mp3')
        if music:
            music.play()

class MusicWindow(App):
    def build(self):
        return MyFloatLayout()
 
if __name__ == "__main__":
    window = MusicWindow()
    window.run()