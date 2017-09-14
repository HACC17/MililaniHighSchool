from kivy.app import App
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.base import runTouchApp
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

import os.path
from kivy.resources import resource_add_path

kv_files = os.path.abspath(os.path.join(os.path.dirname(__file__), 'Kivy'))

resource_add_path(kv_files)

root = BoxLayout()


class Phone(FloatLayout):
    pass
    
class CustomDropDown(Dropdown):
    pass

dropdown = CustomDropDown()
mainbutton = Button(text='Hello', size_hint=(None, None))
mainbutton.bind(on_release=dropdown.open)
dropdown.bind(on_select=lambda instance, x: setattr(mainbutton, 'text', x))

#Builder.load_file('Dropdown.kv') not needed for now
Builder.load_file('Screen_Manager.kv')




class TestApp(App):
    def build(self):
        return Phone()

if __name__ == '__main__':
    TestApp().run()