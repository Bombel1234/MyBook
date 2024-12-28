from Model.base_model import BaseScreenModel


class HomeScreenModel(BaseScreenModel):
    """
    Implements the logic of the
    :class:`~View.HomeScreen.home_screen.HomeScreenView` class.
    """

    def __init__(self, database):
        # Just an example of the data. Use your own values.
        self.base = database
        self.background = 'assets/images/library.png'
        self.data_default_settings()

    def data_from_base_category(self):
        all_table_category = self.base.cursor.execute("SELECT * FROM category").fetchall()
        return all_table_category

    def is_table_category(self):
        result = self.base.cursor.execute(
            f"SELECT name FROM sqlite_master WHERE type='table' AND name='category'"
        ).fetchone()
        return result

    def all_list_category(self, category):
        res = [i[0] for i in self.base.cursor.execute(f"SELECT origin_category FROM category").fetchall()]
        if category in res:
            return False
        return True

    def edit_category(self, stare_value, now_value):
        stare_table_name = str(stare_value).lower().replace(' ', '')
        now_table_name = str(now_value).lower().replace(' ', '')
        self.base.cursor.execute(
            f"UPDATE category SET origin_category='{now_value}',"
            f" key_category='{now_table_name}' WHERE origin_category='{stare_value}'"
        )
        self.base.cursor.execute(f"ALTER TABLE {stare_table_name} RENAME TO {now_table_name}")

        self.base.connect.commit()

    def delete_category_table(self, category, name_table):
        self.base.cursor.execute(
            f"DELETE FROM category WHERE origin_category='{category}'"
        )
        self.base.cursor.execute(
            f"DROP TABLE {name_table}"
        )
        self.base.connect.commit()

    def select_lang(self):
        language = self.base.cursor.execute(
            "SELECT language FROM settings"
        ).fetchone()
        return language[0]

    def data_default_settings(self):
        data = self.base.cursor.execute("SELECT * FROM settings").fetchall()
        if len(data) < 1:
            self.save_default_settings()
        return data

    def save_default_settings(self):
        self.base.cursor.execute(f"INSERT INTO settings VALUES(?,?,?,?,?)",
                                 ('default', 'Light', 'Pl', 1000, 'Blue'))
        self.base.connect.commit()
