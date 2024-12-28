from kivymd.uix.list import BaseListItem, IRightBodyTouch, TwoLineRightIconListItem
from kivymd.uix.selectioncontrol import MDSwitch
from kivy.properties import BooleanProperty


class BaseListItemWithSwitch(BaseListItem):
    active = BooleanProperty(False)

    def __init__(self, **kwargs):
        super(BaseListItemWithSwitch, self).__init__(**kwargs)
        self.register_event_type('on_active')

    def on_active(self, obj, active):
        if active:
            self.active = True
        else:
            self.active = False
        return self.active


class RightSwitchContainer(IRightBodyTouch, MDSwitch):
    pass


class TwoLineListItemWithSwitch(TwoLineRightIconListItem, BaseListItemWithSwitch):
    pass
