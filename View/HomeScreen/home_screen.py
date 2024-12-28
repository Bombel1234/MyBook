from kivy.properties import StringProperty
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog

from View.base_screen import BaseScreenView
from View.HomeScreen.components import ListCategory
from View.HomeScreen.components import ContentEdit
from kivy.storage.jsonstore import JsonStore
import json


class HomeScreenView(BaseScreenView):
    dialog = None
    dialog_delete = None
    img = StringProperty()
    title_screen = StringProperty()
    list_word = []

    def model_is_changed(self) -> None:
        """
        Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.
        """

    def on_pre_enter(self, *args):
        with open('language.json', encoding='utf-8') as f:
            res = json.load(f)
        select_lang = self.model.select_lang()
        if select_lang == 'Pl':
            self.title_screen = res['pl']['screen_home'][0]
            self.language(res['pl']['screen_home'])
        else:
            self.title_screen = res['ukr']['screen_home'][0]
            self.language(res['ukr']['screen_home'])

    def language(self, data):
        self.list_word = data
        return self.list_word

    def on_leave(self, *args):
        if self.ids.box.children:
            self.ids.box.clear_widgets()

    def on_enter(self, *args):
        self.create_card_category()
        self.img = self.model.background

    def create_card_category(self):
        is_table = self.model.is_table_category()
        if is_table is not None:
            data = self.model.data_from_base_category()
            keys = ['key_category', 'origin_category']
            result = [dict(zip(keys, values)) for values in data]
            for i in result:
                obj = ListCategory()
                obj.ids.label_text.text = i['origin_category']
                callback_card = self.controller.on_click_card
                obj.bind(on_press=lambda x=obj: callback_card(x))
                callback_edit = self.controller.on_click_edit
                obj.ids.btn_edit.bind(on_release=lambda x=obj: callback_edit(x))
                callback_delete = self.controller.on_click_delete
                obj.ids.btn_delete.bind(on_release=lambda x=obj: callback_delete(x))
                self.ids.box.add_widget(obj)

    def click_category(self, text_url):
        key = str(text_url).lower().replace(' ', '')
        store = JsonStore('category.json', indent=True)
        store.put('category', category=key)
        store.put('origin_category', origin_category=text_url)
        self.controller.back_screen_category()

    def open_instructions(self):
        pass

    def open_dialog_edit(self, category, obj_edit):
        content_cls = ContentEdit(text=category)
        self.dialog = MDDialog(
            auto_dismiss=False,
            title=self.list_word[1],
            type="custom",
            content_cls=content_cls,
            buttons=[
                MDFlatButton(
                    text=self.list_word[2],
                    theme_text_color="Custom",
                    text_color='black',
                    md_bg_color='grey',
                    on_release=self.close_dialog,
                ),
                MDFlatButton(
                    text=self.list_word[3],
                    theme_text_color="Custom",
                    text_color='black',
                    md_bg_color='green',
                    on_release=lambda x: self.edit_category(x, content_cls, obj_edit)
                ),
            ],
        )
        self.dialog.open()

    def close_dialog(self, obj):
        self.dialog.dismiss()

    def edit_category(self, button, content, obj_edit):
        stare_value = content.text
        now_value = content.ids.input_text.text
        if self.model.all_list_category(now_value):
            self.model.edit_category(stare_value, now_value)
            obj_edit.ids.label_text.text = now_value
            self.dialog.dismiss()
        else:
            self.dialog.dismiss()

    def open_dialog_delete(self, category, name_table, obj_category):
        self.dialog_delete = MDDialog(
            title=self.list_word[4],
            text=f"{self.list_word[5]} {category}???",
            buttons=[
                MDFlatButton(
                    text=self.list_word[2],
                    theme_text_color="Custom",
                    text_color=self.theme_cls.primary_color,
                    on_release=self.close_dialog_delete
                ),
                MDFlatButton(
                    text=self.list_word[6],
                    theme_text_color="Custom",
                    text_color=self.theme_cls.primary_color,
                    on_release=lambda x: self.delete_category(x, category, name_table, obj_category)
                ),
            ],
        )
        self.dialog_delete.open()

    def close_dialog_delete(self, *args):
        self.dialog_delete.dismiss()

    def delete_category(self, button, category, name_table, obj_category):
        self.ids.box.remove_widget(obj_category)
        self.model.delete_category_table(category, name_table)
        self.dialog_delete.dismiss()
