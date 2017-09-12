from kivy.uix.image import Image
from kivy.uix.behaviors import ToggleButtonBehavior

class OptionsButton(ToggleButtonBehavior, Image):
    def __init__(self, **kwargs):
        super(OptionsButton, self).__init__(**kwargs)
        self.source = 'atlas://data/images/defaulttheme/checkbox_off'

    def on_state(self, widget, value):
        if value == 'down':
            self.source = 'atlas://data/images/defaulttheme/checkbox_on'
        else:
            self.source = 'atlas://data/images/defaulttheme/checkbox_off'
