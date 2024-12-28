from Model.base_model import BaseScreenModel


class SettingsScreenModel(BaseScreenModel):
    """
    Implements the logic of the
    :class:`~View.AddLinkScreen.add_link_screen.AddLinkScreenView` class.
    """

    def __init__(self, database):
        # Just an example of the data. Use your own values.
        self.base = database
        self.primary_palette = [
            'Red', 'Pink', 'Purple', 'DeepPurple', 'Indigo', 'Blue', 'LightBlue', 'Cyan', 'Teal', 'Green', 'LightGreen',
            'Lime', 'Yellow', 'Amber', 'Orange', 'DeepOrange', 'Brown', 'Gray', 'BlueGray'
        ]


    def data_default_settings(self):
        data = self.base.cursor.execute("SELECT * FROM settings").fetchall()
        return data

    def select_list_category(self):
        a = []
        for category in self.base.cursor.execute("SELECT * FROM category").fetchall():
            a.append(category[1])
        return a

    def delete_category(self, category):
        name_table = str(category).lower().replace(' ', '')
        self.base.cursor.execute(f"DELETE FROM category WHERE origin_category='{category}'")
        self.base.cursor.execute(f"DROP TABLE {name_table}")
        self.base.connect.commit()

    def add_theme(self, theme):
        self.base.cursor.execute(
            f"UPDATE settings SET theme='{theme}'"
        )
        self.base.connect.commit()

    def select_language(self, language):
        self.base.cursor.execute(
            f"UPDATE settings SET language='{language}'"
        )
        self.base.connect.commit()

    def select_palette_color(self, color):
        self.base.cursor.execute(
            f"UPDATE settings SET palette_color='{color}'"
        )
        self.base.connect.commit()

    def select_lang(self):
        language = self.base.cursor.execute(
            "SELECT language FROM settings"
        ).fetchone()
        return language[0]


