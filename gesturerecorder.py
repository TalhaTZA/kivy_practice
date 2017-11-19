from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.floatlayout import FloatLayout
import kivy.uix , math
from kivy.graphics import Line , Ellipse
from kivy.gesture import Gesture , GestureDatabase
from kivy.uix.screenmanager import ScreenManager ,Screen
from kivy.graphics import Color


class GestureRecorder(Screen):
    
    def on_touch_down(self,touch):
        self.points = [touch.pos]
        color_picker=self.color_picker
        with self.canvas:
            Color(*color_picker.color)
            Ellipse(pos=(touch.x-5,touch.y-5),size=(10,10))
            self.Line=Line(points=(touch.x,touch.y),width=1.5)
    
    def on_touch_move(self,touch):
        self.points+=[touch.pos]
        self.Line.points+=[touch.x,touch.y]

    def on_touch_up(self,touch):
        self.points+=[touch.pos]
        with self.canvas:
            Ellipse(pos=(touch.x-5,touch.y-5),size=(10,10))
        gesture=Gesture()
        gesture.add_stroke(self.points)
        gesture.normalize()
        gdb=GestureDatabase()
        #print ("Gesture:",gdb.gesture_to_str(gesture).decode(encoding='UTF-8',))
        #for ele in self.points:
            #print(ele)

class MultipleScreens(ScreenManager):
    pass

class GestureRecorderApp(App):
    def build(self):
        return MultipleScreens()

if __name__ in ("__main__"):
    GestureRecorderApp().run()