from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout

class DrawingSpace1(RelativeLayout):
    pass

class Drawing1App(App):
    def build(self):
        return DrawingSpace1()

if __name__ == '__main__':
    Drawing1App().run()
