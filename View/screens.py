# The screens dictionary contains the objects of the models and controllers
# of the screens of the application.
from Controller.settings_sreen import SettingsScreenController
from Model.home_screen import HomeScreenModel
from Controller.home_screen import HomeScreenController
from Model.add_link_screen import AddLinkScreenModel
from Controller.add_link_screen import AddLinkScreenController
from Model.resultation_screen import ResultationScreenModel
from Controller.resultation_screen import ResultationScreenController
from Model.settings_screen import SettingsScreenModel

screens = {
    "home screen": {
        "model": HomeScreenModel,
        "controller": HomeScreenController,
    },

    "add link screen": {
        "model": AddLinkScreenModel,
        "controller": AddLinkScreenController,
    },

    "resultation screen": {
        "model": ResultationScreenModel,
        "controller": ResultationScreenController,
    },

    "settings screen": {
        "model": SettingsScreenModel,
        "controller": SettingsScreenController,
    },
}
