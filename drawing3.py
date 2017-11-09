from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout

class DrawingSpace3(RelativeLayout):
    pass

class Drawing3App(App):
    def build(self):
        return DrawingSpace3()

if __name__ == '__main__':
    Drawing3App().run()
