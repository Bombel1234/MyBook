from View.HomeScreen.home_screen import HomeScreenView
from View.HomeScreen.components import ListCategory


class HomeScreenController:
    """
    The `HomeScreenController` class represents a controller implementation.
    Coordinates work of the view with the model.
    The controller implements the strategy pattern. The controller connects to
    the view to control its actions.
    """

    def __init__(self, model):
        self.model = model  # Model.home_screen.HomeScreenModel
        self.view = HomeScreenView(controller=self, model=self.model)

    def get_view(self) -> HomeScreenView:
        return self.view

    def move_screen_add_link(self):
        self.view.parent.current = 'add link screen'

    def go_screen_settings(self):
        self.view.parent.current = 'settings screen'

    def open_dialog_info(self):
        self.view.open_instructions()

    def on_click_edit(self, instance: ListCategory):
        category = instance.parent.parent.ids.label_text.text
        obj_edit = instance.parent.parent
        self.view.open_dialog_edit(category, obj_edit)

    def on_click_card(self, instance: ListCategory):
        text_url = instance.ids.label_text.text
        self.view.click_category(text_url)

    def back_screen_category(self):
        self.view.parent.current = 'resultation screen'

    def on_click_delete(self, instance):
        category = instance.parent.parent.ids.label_text.text
        name_table = str(category).lower().replace(' ', '')
        obj_category = instance.parent.parent
        self.view.open_dialog_delete(category, name_table, obj_category)

