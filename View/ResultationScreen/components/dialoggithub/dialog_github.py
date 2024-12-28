from kivy.properties import StringProperty
from kivy.uix.popup import Popup
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.dialog import MDDialog
from kivymd.uix.textfield import MDTextField
from kivy.uix.widget import Widget


class DialogGithub(Popup, Widget):
    title_git = StringProperty()
    text = StringProperty()
    text_btn = StringProperty()
    link_input = StringProperty()
    btn_link = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

