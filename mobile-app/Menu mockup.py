from kivy.app import App
from kivy.base import runTouchApp
from kivy.lang import Builder
from kivy.properties import ListProperty
from kivy.uix.boxlayout import BoxLayout

from kivy.uix.textinput import TextInput

from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition

import time
import random

class MenuScreen(Screen):
    pass
    
class Screen2(Screen):
    pass

class Screen3(Screen):
    pass

class MyScreenManager(ScreenManager):
    def new_colour_screen(self):
        name = str(time.time())
        s = ColourScreen(name=name,
                         colour=[random.random() for _ in range(3)] + [1])
        self.add_widget(s)
        self.current = name
        
root_widget = Builder.load_string('''
#:import FadeTransition kivy.uix.screenmanager.FadeTransition
MyScreenManager:
    transition: FadeTransition()
    MenuScreen:
    Screen2:
    Screen3:
    
<MenuScreen>:
    name: 'Screenone'
    BoxLayout:
        orientation: 'vertical'
        Button:
            text: 'one'
            font_size: 30
            on_release: app.root.current = 'Screen2'
        Button:
            text: 'two'
            font_size: 30
            on_release: app.root.current = 'PAGE_NEEDED'
        Button:
            text: 'three'
            font_size: 30
            on_release: app.root.current = 'PAGE_NEEDED'
        Button:
            text: 'four'
            font_size: 30
            on_release: app.root.current = 'PAGE_NEEDED'
        Button:
            text: 'five'
            font_size: 30
            on_release: app.root.current = 'PAGE_NEEDED'
        Button:
            text: 'six'
            font_size: 30
            on_release: app.root.current = 'PAGE_NEEDED'
<Screen2>:
    name: 'Screen2'
    BoxLayout:
        orientation: 'vertical'
        Button:
            text: 'type_one'
            font_size: 30
            on_release: app.root.current = 'Screen3'
<Screen3>:
    name: 'Screen3'
    BoxLayout:
        orientation: 'vertical'
        Button:
            text: 'input goes here'
            font_size: 30
                    
''')


class ScreenManagerApp(App):
    def build(self):
        return root_widget

ScreenManagerApp().run()