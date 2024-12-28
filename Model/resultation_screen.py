from Model.base_model import BaseScreenModel


class ResultationScreenModel(BaseScreenModel):
    """
    Implements the logic of the
    :class:`~View.ResultationScreen.resultation_screen.ResultationScreenView` class.
    """

    def __init__(self, database):
        # Just an example of the data. Use your own values.
        self.base = database

    def add_date_in_bases(self, name_table, url, my_text):
        self.base.cursor.execute(f"INSERT INTO {name_table} VALUES(?,?,?,?,?)",
                                 (url, my_text, None, None, None))
        self.base.connect.commit()

    def or_is_url_in_all_base(self, url):
        name_table = [
            i[0] for i in self.base.cursor.execute("SELECT key_category FROM category").fetchall()
        ]
        data_from_tables = [
            self.base.cursor.execute(f"SELECT url FROM {j} WHERE url='{url}'").fetchone() for j in
            name_table
        ]
        b = []
        for item in data_from_tables:
            if item is not None:
                index = data_from_tables.index(item)
                b.append(name_table[index])
        if len(b) > 0:
            return True
        else:
            return False

    def data_from_name_table(self, name_table):
        data = self.base.cursor.execute(f"SELECT * FROM {name_table}").fetchall()
        keys = ['url', 'tres', 'is_img', 'path_img', 'name_img']
        result = [dict(zip(keys, values)) for values in data]
        return result

    def or_is_table_in_base(self, name_table):
        result = self.base.cursor.execute(
            f"SELECT name FROM sqlite_master WHERE type='table' AND name='{name_table}'"
        ).fetchone()
        return result

    def delete_card(self, name_table, text_url):
        self.base.cursor.execute(
            f"DELETE FROM {name_table} WHERE now='{text_url}'"
        )
        self.base.connect.commit()

    def update_text(self, name_table, value, now_value):
        self.base.cursor.execute(
            f"UPDATE {name_table} SET now='{now_value}' WHERE now='{value}'"
        )
        self.base.connect.commit()

    def all_text_url(self, name_table, text_url):
        res = [i[0] for i in self.base.cursor.execute(f"SELECT now FROM {name_table}").fetchall()]
        if text_url in res:
            return False
        return True

    def selected_url_origin(self, name_table, text_url):
        res = self.base.cursor.execute(
            f"SELECT url FROM {name_table} WHERE now='{text_url}'"
        ).fetchone()
        return res[0]

    def add_image_path(self, name_table, url_img, key_card):
        self.base.cursor.execute(
            f"UPDATE {name_table} SET is_img='es', name_img='{url_img}'"
            f"WHERE now='{key_card}'"
        )
        self.base.connect.commit()

    def select_lang(self):
        language = self.base.cursor.execute(
            "SELECT language FROM settings"
        ).fetchone()
        return language[0]








