import os.path
import sqlite3


from android import mActivity


class DataBase:
    name = "RestDB"

    def __init__(self):
        context = mActivity.getApplicationContext()
        self.result =  context.getExternalFilesDir(None)
        self.storage_path =  str(self.result.toString())
        self.connect = sqlite3.connect(f'{self.storage_path}/main_base.db')
        self.cursor = self.connect.cursor()
        self.create_table_settings()
        self.create_table_category()
        self.data_settings()

    def data_settings(self):
        res = self.cursor.execute('SELECT * FROM settings').fetchall()
        return res

    def create_table_category(self):
        self.cursor.execute('''
                        CREATE TABLE IF NOT EXISTS category(
                            key_category TEXT NOT NULL,
                            origin_category TEXT NOT NULL
                        )
                        ''')
        self.connect.commit()

    def create_table_settings(self):
        self.cursor.execute('''
                        CREATE TABLE IF NOT EXISTS settings(
                            setting TEXT NOT NULL,
                            theme TEXT NOT NULL,
                            language TEXT NOT NULL,
                            height_card INT NOT NULL,
                            palette_color TEXT NOT NULL
                        )
                        ''')
        self.connect.commit()
