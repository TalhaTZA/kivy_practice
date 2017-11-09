from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout

class DrawingSpace2(RelativeLayout):
    pass

class Drawing2App(App):
    def build(self):
        return DrawingSpace2()

if __name__ == '__main__':
    Drawing2App().run()
