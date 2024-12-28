from kivy.uix.behaviors.button import ButtonBehavior
from kivymd.uix.card import MDCard


class ListCategory(MDCard, ButtonBehavior):

    def __init__(self, **kwargs):
        super(ListCategory, self).__init__(**kwargs)
