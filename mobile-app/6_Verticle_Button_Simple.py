import kivy
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.app import App
from kivy.uix.button import Button

class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        btn1 = Button(text='1')
        btn2 = Button(text='2')
        btn3 = Button(text='3')
        btn4 = Button(text='4')
        btn5 = Button(text='5')
        btn6 = Button(text='6')
        layout.add_widget(btn1)
        layout.add_widget(btn2)
        layout.add_widget(btn3)
        layout.add_widget(btn4)
        layout.add_widget(btn5)
        layout.add_widget(btn6)
        
        
        return layout

MyApp().run()