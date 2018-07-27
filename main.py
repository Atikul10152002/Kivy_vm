#from __future__ import print_function

from kivy.app import App
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.widget import Widget
from kivy.graphics import Line
from kivy.clock import Clock
from kivy.properties import NumericProperty, ListProperty, ObjectProperty
from kivy.animation import Animation
from random import randint
from kivy.clock import Clock
from kivy.core.window import Window

# from kivy.uix.widget import Widget
# from kivy.uix.floatlayout import FloatLayout
# from kivy.graphics import Color, Ellipse, Line
# from kivy.uix.image import Image
# from kivy.uix.label import Label
# from kivy.uix.button import Button


class MainScreen(Screen):
    center = ListProperty([Window.width/2, Window.height/2])
    pass

class Rect(Widget):
    _height= _width = NumericProperty(randint(5,30))
    def __init__(self, **kw):
        super(Rect,self).__init__(**kw)
        self._height= self._width = randint(5,30)
        Clock.schedule_interval(self.cool_anim,1/60)
    def cool_anim(self, *ag):
        self.y += 1
        if self.y>=Window.height:
            
        # Animation.cancel_all(self)
        # anim = Animation(
        #     x = randint(0, round(Window.width)),
        #     y = randint(0, round(Window.height)), 
        #     duration=4, 
        #     t="out_elastic")
        # anim.start(self)
    def on_touch_down(self, touch):
        self.cool_anim()

class GameScreen(Screen):
    pass

class Widg(Widget):
    def __init__(self, **kw):
        super(Widg,self).__init__(**kw)
        self.add_widget(Rect())
        
class ScreenManagement(ScreenManager):
    pass

Presentation = Builder.load_file("MyPaint.kv")


class MyPaintApp(App):
    def build(self):
        return Presentation


if __name__ == '__main__':
    MyPaintApp().run()