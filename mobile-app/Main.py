from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


class LoginScreen(GridLayout):

    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.cols = 2
        self.spacing = 10
        
        self.add_widget(Label(text='Todays Shower Duration', size_hint_x=None, width=300))
        self.showerDuration = TextInput(multiline=False, size_hint_x=None, width=300)
        self.add_widget(self.showerDuration)
        
        self.add_widget(Label(text='Most Recent Water Bill', size_hint_x=None, width=300))
        self.waterBill = TextInput(multiline=False, size_hint_x=None, width=300)
        self.add_widget(self.waterBill)

        self.add_widget(Label(text='That Bills Date', size_hint_x=None, width=300))
        self.waterBillDate = TextInput(multiline=False, size_hint_x=None, width=300)
        self.add_widget(self.waterBillDate)


class MyApp(App):

    def build(self):
        return LoginScreen()


MyApp().run()
