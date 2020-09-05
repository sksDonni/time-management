import sqlite3
import json
import logging


def parse_json(path):
    with open(path) as file:
        data = json.load(file)
    return data


class Database:
    def __init__(self, db_name=":memory:"):
        try:
            self.__db_name = db_name
            self.__connection = sqlite3.connect(self.__db_name)
            self.__cursor = self.__connection.cursor()
        except ValueError:
            logging.error("Unable to initialize database!")

    def get_db_name(self):
        return self.__db_name

    def get_connection(self):
        return self.__connection

    def get_cursor(self):
        return self.__cursor

    def disconnect(self):
        self.get_connection().close


class DataDefinitionLanguage:
    def __init__(self, database):
        self.database = database
        self.connection = database.get_connection()
        self.cursor = database.get_cursor()

    def strip_brackets_and_colons(self, query):
        return query.replace("{", "").replace("}", "").replace(":", "")

    def create_sql(self, table, schema):
        query = f"CREATE TABLE IF NOT EXISTS {table} ({schema})"
        return self.strip_brackets_and_colons(query)

    def create_table(self, table, schema):
        self.cursor.execute(self.create_sql(table, schema))
        self.connection.commit()

    def drop_table(self, table):
        query = f"DROP TABLE {table}"
        self.cursor.execute(query)
