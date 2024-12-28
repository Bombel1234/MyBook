import json

from kivy.properties import StringProperty
from kivymd.uix.dialog import MDDialog
from kivymd.toast import toast
from View.base_screen import BaseScreenView
from kivy.clock import Clock


class AddLinkScreenView(BaseScreenView):
    title_screen = StringProperty()
    title = StringProperty()
    input_text = StringProperty()
    text_btn = StringProperty()
    list_word = []

    def on_pre_enter(self, *args):
        with open('language.json', encoding='utf-8') as f:
            res = json.load(f)
        select_lang = self.model.select_lang()
        if select_lang == 'Pl':
            self.title_screen = res['pl']['screen_add_category'][0]
            t1 = res['pl']['screen_add_category'][1][0]
            t2 = res['pl']['screen_add_category'][1][1]
            self.title = f'[color=ff3333]{t1}[/color][color=3333ff]{t2}[/color]'
            self.input_text = res['pl']['screen_add_category'][2]
            self.text_btn = res['pl']['screen_add_category'][3]
            self.language(res['pl']['screen_add_category'])
        else:
            self.title_screen = res['ukr']['screen_add_category'][0]
            t1 = res['ukr']['screen_add_category'][1][0]
            t2 = res['ukr']['screen_add_category'][1][1]
            self.title = f'[color=ff3333]{t1}[/color][color=3333ff]{t2}[/color]'
            self.input_text = res['ukr']['screen_add_category'][2]
            self.text_btn = res['ukr']['screen_add_category'][3]
            self.language(res['ukr']['screen_add_category'])

    def language(self, data):
        self.list_word = data
        return self.list_word

    def add_category(self, category, input_obj):
        key_category = str(category).lower().replace(' ', '')
        if key_category != '':
            if str(key_category).isdigit():
                input_obj.error = True
            else:
                if self.model.add_category(key_category, category):
                    toast(f'{self.list_word[4]}!!!')
                    self.model.create_table_category(key_category)
                    Clock.schedule_once(self.back_screen_home, 1.5)
                else:
                    MDDialog(title=f'{self.list_word[5]}').open()
        else:
            input_obj.error = True

    def back_screen_home(self, dt):
        self.parent.current = 'home screen'
