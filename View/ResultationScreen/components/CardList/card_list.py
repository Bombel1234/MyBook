
from kivymd.uix.card import MDCard
from kivy.properties import StringProperty


class CardList(MDCard):
    text = StringProperty()
    img_path = StringProperty()

    def __init__(self, **kwargs):
        super(CardList, self).__init__(**kwargs)


