from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder

Builder.load_string("""

<GridLayout>:
    cols:2
    Label:
        color: .8,.9,0,1
        canvas:
            Color:
                rgba: .5,.5,.5,1
            Rectangle:
                pos: self.x+10 , self.y+10
                size: self.width - 20  , self.height-20
        text: 'sdadadad'
    Widget:
        canvas:
            Rectangle:
                pos: self.x+10 , self.y+10
                size: self.width - 20  , self.height-20
""")


class LabelApp(App):
    def build(self):
        return GridLayout()

if __name__ in ('__main__'):
    LabelApp().run()