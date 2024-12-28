from kivy.properties import StringProperty
from kivymd.uix.boxlayout import MDBoxLayout


class ContentEdit(MDBoxLayout):
    text = StringProperty()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.register_event_type('on_release')

    def on_release(self, *args):
        """
        Handle
        """