from kivy.app import App
from kivy.base import runTouchApp
from kivy.lang import Builder
from kivy.properties import ListProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.base import runTouchApp
from kivy.uix.textinput import TextInput

import os.path
from kivy.resources import resource_add_path

kv_files = os.path.abspath(os.path.join(os.path.dirname(__file__), 'Kivy'))




resource_add_path(kv_files)


from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition

import time
import random

class MenuScreen(Screen):
    pass
    
class Screen2(Screen):
    pass

class Screen3(Screen):
    pass
    
class CustomDropDown(DropDown):
    pass

class MyScreenManager(ScreenManager):
    def new_colour_screen(self):
        name = str(time.time())
        s = ColourScreen(name=name,
                         colour=[random.random() for _ in range(3)] + [1])
        self.add_widget(s)
        self.current = name
        

dropdown = CustomDropDown()
mainbutton = Button(text='Hello', size_hint=(None, None))
mainbutton.bind(on_release=dropdown.open)
dropdown.bind(on_select=lambda instance, x: setattr(mainbutton, 'text', x))
        
dropdown = DropDown()
        
root_widget = Builder.load_file("Screen.kv")


class ScreenManagerApp(App):
    def build(self):
        return root_widget

ScreenManagerApp().run()