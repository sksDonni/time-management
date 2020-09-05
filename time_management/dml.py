import logging


class DataManipulationLanguage:
    def __init__(self, database):
        self.database = database
        self.connection = database.get_connection()
        self.cursor = database.get_cursor()

    def select_star_sql(self, table):
        query = f"SELECT * FROM {table}"
        try:
            self.cursor.execute(query)
        except ValueError:
            logging.error("Unable to execute query!")
        return self.cursor.fetchall()
