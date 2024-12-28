import json

from kivy.properties import StringProperty
from kivymd.effects.fadingedge import FadingEdgeEffect
from kivymd.effects.roulettescroll import RouletteScrollEffect
from kivymd.uix.button import MDTextButton
from kivy.uix.scrollview import ScrollView

from View.SettingsScreen.components import TwoLineListItemWithSwitch  # NOQA
from View.base_screen import BaseScreenView


class FadeScrollView(RouletteScrollEffect, FadingEdgeEffect, ScrollView):
    pass


class SettingsScreenView(BaseScreenView):
    title_screen = StringProperty()
    theme = StringProperty()
    lang = StringProperty()
    palette_color = StringProperty()
    select_color = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.all_button_palette = []
        self.list_word = []
        self.json_file = None

    def model_is_changed(self) -> None:
        """
        Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.
        """

    def on_enter(self, *args):
        pass

    def on_pre_enter(self, *args):
        self.add_colors_palette()
        data = self.model.data_default_settings()
        self.ids.item2.secondary_text = data[0][2]
        self.select_color = data[0][4]
        with open('language.json', encoding='utf-8') as f:
            self.json_file = json.load(f)
        select_lang = self.model.select_lang()
        if select_lang == 'Pl':
            self.title_screen = self.json_file['pl']['screen_settings'][0]
            self.theme = self.json_file['pl']['screen_settings'][1]
            self.lang = self.json_file['pl']['screen_settings'][4]
            self.palette_color = self.json_file['pl']['screen_settings'][5]
            self.ids.item2.secondary_text = self.json_file['pl']['screen_settings'][6]
            if self.theme_cls.theme_style == "Dark":
                self.ids.item1.secondary_text = self.json_file['pl']['screen_settings'][2]
            else:
                self.ids.item1.secondary_text = self.json_file['pl']['screen_settings'][3]

            self.language(self.json_file['pl']['screen_settings'])
        else:
            self.title_screen = self.json_file['ukr']['screen_settings'][0]
            self.theme = self.json_file['ukr']['screen_settings'][1]
            self.lang = self.json_file['ukr']['screen_settings'][4]
            self.palette_color = self.json_file['ukr']['screen_settings'][5]
            if self.theme_cls.theme_style == "Dark":
                self.ids.item1.secondary_text = self.json_file['ukr']['screen_settings'][2]
            else:
                self.ids.item1.secondary_text = self.json_file['ukr']['screen_settings'][3]
            self.ids.item2.secondary_text = self.json_file['ukr']['screen_settings'][6]

            self.language(self.json_file['ukr']['screen_settings'])

    def language(self, data):
        self.list_word = data
        return self.list_word

    def update_language(self, language):
        if language == 'Pl':
            self.ids.item2.secondary_text = 'Pl'
            self.title_screen = self.json_file['pl']['screen_settings'][0]
            self.theme = self.json_file['pl']['screen_settings'][1]
            self.lang = self.json_file['pl']['screen_settings'][4]
            self.palette_color = self.json_file['pl']['screen_settings'][5]
            self.ids.item2.secondary_text = self.json_file['pl']['screen_settings'][6]
            if self.theme_cls.theme_style == "Dark":
                self.ids.item1.secondary_text = self.json_file['pl']['screen_settings'][2]
            else:
                self.ids.item1.secondary_text = self.json_file['pl']['screen_settings'][3]
        else:
            self.ids.item2.secondary_text = 'Ukr'
            self.title_screen = self.json_file['ukr']['screen_settings'][0]
            self.theme = self.json_file['ukr']['screen_settings'][1]
            self.lang = self.json_file['ukr']['screen_settings'][4]
            self.palette_color = self.json_file['ukr']['screen_settings'][5]
            self.ids.item2.secondary_text = self.json_file['ukr']['screen_settings'][6]
            if self.theme_cls.theme_style == "Dark":
                self.ids.item1.secondary_text = self.json_file['ukr']['screen_settings'][2]
            else:
                self.ids.item1.secondary_text = self.json_file['ukr']['screen_settings'][3]


    def on_leave(self, *args):
        self.ids.box_palette.clear_widgets()
        self.all_button_palette.pop()

    def add_colors_palette(self):
        for color in self.model.primary_palette:
            text_button = color
            button = MDTextButton(text=text_button, font_size='20sp')
            button.bind(on_press=lambda x: self.click_button_palette(x, self.all_button_palette))
            self.ids.box_palette.add_widget(button)
            self.all_button_palette.append(button)

    def click_button_palette(self, obj, all_btn):
        button_text = obj.text
        for button in all_btn:
            button.md_bg_color = [1, 1, 1, 0]
        obj.md_bg_color = (0, 1, 0, 1)
        self.select_color = button_text
        self.theme_cls.primary_palette = button_text
        self.model.select_palette_color(button_text)

    def switch_theme_select(self, obj, active):
        select_lang = self.model.select_lang()
        if active:
            self.theme_cls.theme_style = 'Dark'
            self.model.add_theme('Dark')
            self.update_language(select_lang)

        else:
            self.theme_cls.theme_style = 'Light'
            self.model.add_theme('Light')
            self.update_language(select_lang)

    def switch_language_select(self, obj, active):
        if not active:
            self.model.select_language('Ukr')
            self.update_language('Ukr')
        else:
            self.model.select_language('Pl')
            self.update_language('Pl')
