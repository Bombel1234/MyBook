from urllib.parse import urljoin

import requests
from kivy.logger import Logger

from View.ResultationScreen.resultation_screen import ResultationScreenView

from View.ResultationScreen.components import CardList


class ResultationScreenController:
    """
    The `ResultationScreenController` class represents a controller implementation.
    Coordinates work of the view with the model.
    The controller implements the strategy pattern. The controller connects to
    the view to control its actions.
    """

    def __init__(self, model):
        self.model = model  # Model.resultation_screen.ResultationScreenModel
        self.view = ResultationScreenView(controller=self, model=self.model)

    def get_view(self) -> ResultationScreenView:
        return self.view

    def on_click_url(self, instance_card: CardList) -> None:
        text_url = instance_card.parent.parent.parent.parent.ids.label.text
        self.view.move_to_link(text_url)

    def on_click_edit(self, instance):
        text_url = instance.parent.parent.parent.parent.ids.label.text
        obj_card = instance.parent.parent.parent.parent
        self.view.open_dialog_edit(text_url, obj_card)

    def on_delete_card(self, instance_card: CardList) -> None:
        text_url = instance_card.parent.parent.parent.parent.ids.label.text
        obj_card = instance_card.parent.parent.parent.parent
        self.view.open_delete_dialog(text_url, obj_card)

    def back_home(self):
        self.view.parent.current = 'home screen'

    def on_click_img(self, button, obj) -> None:
        obj_img = button.parent.parent.parent.parent
        text_url = button.parent.parent.parent.parent.ids.label.text
        self.view.open_dialog_image(text_url, obj_img)

    def add_link(self, instance, obj, name_table, text_url, obj_img):
        html_url_img = obj.ids.id_link.text
        if html_url_img != "":
            if html_url_img[0:19] != "https://github.com/":
                self.view.open_dialog_no_github()
            else:
                first_url = "https://google.com"
                final_url = urljoin(first_url, html_url_img)
                if requests.get(final_url).status_code == 200:
                    self.model.add_image_path(name_table, html_url_img, text_url)
                    obj_img.ids.img.source = f"{html_url_img}/?raw=true"
                    obj.dismiss()
                else:
                    self.view.error_link()
            



