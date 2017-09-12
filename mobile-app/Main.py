from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


class LoginScreen(GridLayout):

    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)

        layout = GridLayout(size_hint_x=None, width=100, row_force_default=True, row_default_height=40)
        self.cols = 2
        self.spacing = 10
        
        self.add_widget(Label(text='Todays Shower Duration'))
        self.showerDuration = TextInput(multiline=False)
        self.add_widget(self.showerDuration)
        
        self.add_widget(Label(text='Most Recent Water Bill'))
        self.waterBill = TextInput(multiline=False)
        self.add_widget(self.waterBill)


class MyApp(App):

    def build(self):
        return LoginScreen()


MyApp().run()
