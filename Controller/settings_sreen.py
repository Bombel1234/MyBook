from View.SettingsScreen.settings_screen import SettingsScreenView


class SettingsScreenController:
    """
    The `HomeScreenController` class represents a controller implementation.
    Coordinates work of the view with the model.
    The controller implements the strategy pattern. The controller connects to
    the view to control its actions.
    """

    def __init__(self, model):
        self.model = model  # Model.home_screen.HomeScreenModel
        self.view = SettingsScreenView(controller=self, model=self.model)



    def get_view(self) -> SettingsScreenView:
        return self.view

    def back_home(self):
        self.view.parent.current = 'home screen'

    def add_instruction(self):
        self.view.save_instruction()

    def switch_value(self, a, active):
        if active:
            self.view.theme_cls.theme_style_switch_animation = True
            self.view.theme_cls.theme_style = 'Dark'
        else:
            self.view.theme_cls.theme_style_switch_animation = True
            self.view.theme_cls.theme_style = 'Light'

    def select_list_category(self):
        self.model.select_list_category()


