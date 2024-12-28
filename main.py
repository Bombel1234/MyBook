"""
The entry point to the application.

The application uses the MVC template. Adhering to the principles of clean
architecture means ensuring that your application is easy to test, maintain,
and modernize.

You can read more about this template at the links below:

https://github.com/HeaTTheatR/LoginAppMVC
https://en.wikipedia.org/wiki/Model–view–controller
"""
import os.path

from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.screenmanager import NoTransition
from kivy.core.window import Window



from View.screens import screens
from Model.database import DataBase

from android import mActivity


Window.softinput_mode = 'below_target'



class BookUrl(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.bind(on_keyboard=self.quit_app)
        self.load_all_kv_files(self.directory)
        # This is the screen manager that will contain all the screens of your
        # application.
        self.manager_screens = ScreenManager(transition=NoTransition())
        self.database = DataBase()

    def build(self) -> ScreenManager:
        self.generate_application_screens()
        self.theme_cls.material_style = 'M3'
        self.theme_cls.theme_style_switch_animation = True
        self.theme_cls.theme_style_switch_animation_duration = 0.8
        self.settings()
        return self.manager_screens

    def settings(self):
        res = self.database.data_settings()
        theme = res[0][1]
        self.theme_cls.theme_style = theme
        self.theme_cls.primary_palette = res[0][4]

    
    
    def quit_app(self, window, key, *args):
        
        if key == 27:
            mActivity.finishAndRemoveTask()
            return True
        else:
            return False

    def generate_application_screens(self) -> None:
        """
        Creating and adding screens to the screen manager.
        You should not change this cycle unnecessarily. He is self-sufficient.

        If you need to add any screen, open the `View.screens.py` module and
        see how new screens are added according to the given application
        architecture.
        """

        for i, name_screen in enumerate(screens.keys()):
            model = screens[name_screen]["model"](self.database)
            controller = screens[name_screen]["controller"](model)
            view = controller.get_view()
            view.manager_screens = self.manager_screens
            view.name = name_screen
            self.manager_screens.add_widget(view)


BookUrl().run()
