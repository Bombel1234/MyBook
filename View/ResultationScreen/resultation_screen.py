import json

import requests
import webbrowser

from kivy.properties import StringProperty
from kivy.storage.jsonstore import JsonStore
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.toast import toast
from urllib.parse import urljoin
from kivy.logger import Logger
from kivy.metrics import dp

from View.base_screen import BaseScreenView

from View.ResultationScreen.components import CardList
from View.ResultationScreen.components import ContentDialog
from View.ResultationScreen.components import DialogGithub
from kivy.animation import Animation


class ResultationScreenView(BaseScreenView):
    dialog_content = None
    dialog_delete = None
    anim = True
    finish_anim = False
    label_url = StringProperty()
    inp1_text = StringProperty()
    label_ops = StringProperty()
    input2_text = StringProperty()
    text_btn = StringProperty()

    def __init__(self, **kw):
        super().__init__(**kw)
        self.animation = None
        self.list_word = None

    def on_pre_enter(self, *args):
        with open('language.json', encoding='utf-8') as f:
            res = json.load(f)
        select_lang = self.model.select_lang()
        if select_lang == 'Pl':
            self.label_url = res['pl']['screen_result'][0]
            self.inp1_text = res['pl']['screen_result'][1]
            self.label_ops = res['pl']['screen_result'][2]
            self.input2_text = res['pl']['screen_result'][3]
            self.text_btn = res['pl']['screen_result'][4]

            self.language(res['pl']['screen_result'])
        else:
            self.label_url = res['ukr']['screen_result'][0]
            self.inp1_text = res['ukr']['screen_result'][1]
            self.label_ops = res['ukr']['screen_result'][2]
            self.input2_text = res['ukr']['screen_result'][3]
            self.text_btn = res['ukr']['screen_result'][4]

            self.language(res['ukr']['screen_result'])

    def language(self, data):
        self.list_word = data
        return self.list_word

    def animation_add_link(self, button, top_box):
        if self.anim:
            self.animation = Animation(pos_hint={'center_x': .5, 'center_y': .5})
            self.animation.bind(on_complete=self.func_finish_anim)
            self.animation.start(button)
            Animation(y=button.top - top_box.height + button.height * 2).start(top_box)
            self.anim = False

    def on_enter(self, *args):
        store = JsonStore('category.json')
        text_topAppbar = store.store_get('origin_category')['origin_category']
        self.ids.tb.title = text_topAppbar.upper()
        self.create_card_list()

    def on_leave(self, *args):
        if self.ids.box_card.children:
            self.ids.box_card.clear_widgets()
        Animation(pos_hint={'center_x': .5, 'center_y': .9}).start(self.ids.btn)
        Animation(y=self.height).start(self.ids.top_box)
        self.anim = True

    def create_card_list(self):
        store = JsonStore('category.json')
        name_table = store.store_get('category')['category']
        is_table = self.model.or_is_table_in_base(name_table)
        if is_table is not None:
            data = self.model.data_from_name_table(name_table)
            for i in enumerate(data):
                obj_card = CardList()
                obj_card.text = i[1]['tres']
                callback_url = self.controller.on_click_url
                obj_card.ids.btn_link.bind(on_release=lambda x=obj_card: callback_url(x))
                callback_delete = self.controller.on_delete_card
                obj_card.ids.btn_delete.bind(on_release=lambda x=obj_card: callback_delete(x))
                callback_edit = self.controller.on_click_edit
                obj_card.ids.btn_edit.bind(on_release=lambda x=obj_card: callback_edit(x))
                callback_img = self.controller.on_click_img
                obj_card.ids.btn_img.bind(on_release=lambda x: callback_img(x, obj_card))

                if i[1]['is_img'] == 'es' and i[1]['name_img'] is not None:
                    url_img = i[1]['name_img']
                    obj_card.img_path = f"{url_img}?raw=true"
                else:
                    obj_card.img_path = 'assets/images/back_card.png'
                self.ids.box_card.add_widget(obj_card)

    def func_finish_anim(self, *args):
        self.finish_anim = True

    def add_url_in_base(self, url, my_text, button, top_box):
        if self.finish_anim:
            store = JsonStore('category.json')
            name_table = store.store_get('category')['category']
            first_url = "https://google.com"
            final_url = urljoin(first_url, url)
            if url != '' and my_text != '':
                res = self.model.or_is_url_in_all_base(url)
                if res:
                    self.ids.inp_url.text = ''
                    MDDialog(title=self.list_word[5]).open()
                else:
                    if requests.get(final_url).status_code == 200:
                        self.model.add_date_in_bases(name_table, url, my_text)
                        obj_card = CardList()
                        obj_card.text = my_text
                        callback_url = self.controller.on_click_url
                        obj_card.ids.btn_link.bind(on_release=lambda x=obj_card: callback_url(x))
                        callback_delete = self.controller.on_delete_card
                        obj_card.ids.btn_delete.bind(on_release=lambda x=obj_card: callback_delete(x))
                        callback_edit = self.controller.on_click_edit
                        obj_card.ids.btn_edit.bind(on_release=lambda x=obj_card: callback_edit(x))
                        callback_img = self.controller.on_click_img
                        obj_card.ids.btn_img.bind(on_release=lambda x: callback_img(x, obj_card))
                        self.ids.box_card.add_widget(obj_card)
                        self.ids.inp_url.text = ''
                        self.ids.inp_tres.text = ''
                        toast(f'{self.list_word[6]}!!!')
                        Animation(pos_hint={'center_x': .5, 'center_y': .9}).start(button)
                        Animation(y=self.height).start(top_box)
                        self.anim = True
                    else:
                        self.ids.inp_url.text = ''
                        self.error_link()

    def error_link(self):
        MDDialog(title=f'{self.list_word[7]}!!!').open()

    def open_dialog_edit(self, text_url, obj_card):
        content_cls = ContentDialog(text=text_url)
        self.dialog_content = MDDialog(
            auto_dismiss=False,
            title=f"{self.list_word[8]}",
            type="custom",
            content_cls=content_cls,
            buttons=[
                MDFlatButton(
                    text=self.list_word[9],
                    theme_text_color="Custom",
                    text_color='black',
                    md_bg_color='grey',
                    on_release=lambda x: self.close_dialog(x)
                ),
                MDFlatButton(
                    text=self.list_word[10],
                    theme_text_color="Custom",
                    text_color='black',
                    md_bg_color='green',
                    on_release=lambda x: self.edit_text(x, text_url, content_cls, obj_card)
                ),
            ],
        )
        self.dialog_content.open()

    def close_dialog(self, x):
        self.dialog_content.dismiss()

    def edit_text(self, instance, text_url, content, obj_card):
        now_value = content.ids.input_text.text
        store = JsonStore('category.json')
        name_table = store.store_get('category')['category']
        self.model.update_text(name_table, text_url, now_value)
        obj_card.ids.label.text = now_value
        self.dialog_content.dismiss()
        toast(self.list_word[11])

    def open_delete_dialog(self, text_url, obj_card):
        self.dialog_delete = MDDialog(
            auto_dismiss=False,
            title=self.list_word[12],
            text=text_url,
            buttons=[
                MDFlatButton(
                    text=self.list_word[9],
                    theme_text_color="Custom",
                    text_color='black',
                    md_bg_color='grey',
                    on_release=self.close_dialog_delete
                ),
                MDFlatButton(
                    text=self.list_word[13],
                    theme_text_color="Custom",
                    text_color='black',
                    md_bg_color='red',
                    on_release=lambda x: self.delete_card(x, text_url, obj_card)
                ),
            ],
        )
        self.dialog_delete.open()

    def close_dialog_delete(self, obj):
        self.dialog_delete.dismiss()

    def delete_card(self, obj, text_url, obj_card):
        store = JsonStore('category.json')
        name_table = store.store_get('category')['category']
        self.model.delete_card(name_table, text_url)
        self.ids.box_card.remove_widget(obj_card)
        toast(self.list_word[14])
        self.dialog_delete.dismiss()

    def move_to_link(self, text_url):
        store = JsonStore('category.json')
        name_table = store.store_get('category')['category']
        link_origin = self.model.selected_url_origin(name_table, text_url)
        webbrowser.open(link_origin)

    def open_dialog_image(self, text_url, obj_img):
        store = JsonStore('category.json')
        name_table = store.store_get('category')['category']
        dialog_github = DialogGithub()
        dialog_github.title_git = self.list_word[15]
        dialog_github.text = self.list_word[16]
        dialog_github.text_btn = self.list_word[17]
        dialog_github.link_input = self.list_word[18]
        dialog_github.btn_link = self.list_word[19]

        callback_btn_add_link = self.controller.add_link
        dialog_github.ids.btn_add_link.bind(on_release=lambda x: callback_btn_add_link(
            x, dialog_github, name_table, text_url, obj_img)
                                            )
        dialog_github.open()

    def open_dialog_no_github(self):
        MDDialog(title=self.list_word[20]).open()
