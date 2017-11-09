from kivy.app import App
from kivy.uix.widget import Widget

class MyWidget2(Widget):
    pass

class Widgets2App(App):
    def build(self):
        return MyWidget2()

if __name__== "__main__":
    Widgets2App().run()