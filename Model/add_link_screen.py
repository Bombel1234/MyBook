from Model.base_model import BaseScreenModel


class AddLinkScreenModel(BaseScreenModel):
    """
    Implements the logic of the
    :class:`~View.AddLinkScreen.add_link_screen.AddLinkScreenView` class.
    """

    def __init__(self, database):
        # Just an example of the data. Use your own values.
        self.base = database

    def add_category(self, key_category, category):
        all_data = self.data_from_base_category()
        if len(all_data) > 0:
            is_category = self.or_is_category_in_table(key_category)
            if is_category:
                return False
            else:
                self.base.cursor.execute(f"INSERT INTO category VALUES(?,?)",
                                         (key_category, category))
                self.base.connect.commit()
                return True

        else:
            self.base.cursor.execute(f"INSERT INTO category VALUES(?,?)",
                                     (key_category, category))
            self.base.connect.commit()
            return True

    def data_from_base_category(self):
        all_table_category = self.base.cursor.execute("SELECT * FROM category").fetchall()
        return all_table_category

    def or_is_category_in_table(self, key_category):
        if self.base.cursor.execute(
                f"SELECT key_category FROM category WHERE key_category='{key_category}'").fetchone():
            return True
        return False

    def create_table_category(self, name_table):
        self.base.cursor.execute(f"CREATE TABLE IF NOT EXISTS {name_table}("
                                 f"url TEXT,"
                                 f"now TEXT,"
                                 f"is_img TEXT,"
                                 f"path_img TEXT,"
                                 f"name_img TEXT)"

                                 )
        self.base.connect.commit()

    def select_lang(self):
        language = self.base.cursor.execute(
            "SELECT language FROM settings"
        ).fetchone()
        return language[0]
