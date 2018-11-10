import sqlite3
import kronos


# Not really the Proxy pattern... more just a class. TODO :: find a better name for this.
class DatabaseProxy:
    rows_in_table = 0
    database_name = "time_management.db"
    table_name = "time_management"
    schema = {"id": "id", "date": "date", "note": "note", "complete_in_days": "complete_in_days",
              "is_complete": "is_complete"}

    def __init__(self):
        self.connection = sqlite3.connect(self.database_name)
        self.cursor = self.connection.cursor()
        self.rows_in_table = self.count_rows()

    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS {}
                            ({} int, {} text, {} text, {} text, {} text)'''.format(self.table_name, *self.schema))
        self.connection.commit()

    def update_table_with_note(self, note):
        self.rows_in_table = self.rows_in_table + 1
        self.cursor.execute(
            "INSERT INTO {} ({}, {}, {}, {}, {}) VALUES (?, ?, ?, ?, ?)".format(self.table_name, *self.schema),
            (self.rows_in_table, kronos.get_date_time(), note, "-1", "-1"))
        self.connection.commit()

    def count_rows(self):
        return len(self.cursor.execute("SELECT * FROM {}".format(self.table_name)).fetchall())

    def update_table_with_todo_and_goal(self, note, completion_goal):
        self.rows_in_table = self.rows_in_table + 1
        self.cursor.execute(
            "INSERT INTO {} ({}, {}, {}, {}, {}) VALUES (?, ?, ?, ?, ?)".format(self.table_name, *self.schema),
            (self.rows_in_table, kronos.get_date_time(), note, completion_goal, "0"))
        self.connection.commit()

    def update_completion(self, row_id):
        self.cursor.execute(
            "UPDATE {} SET {} = {} WHERE id = {}".format(self.table_name, self.schema["is_complete"], 1, row_id))

    def get_all_items(self):
        rows = []
        for row in self.cursor.execute("SELECT * FROM {}".format(self.table_name)):
            rows.append(row)
        return rows

    def get_overdue_items(self):
        rows = []
        for row in self.cursor.execute("SELECT * FROM {}".format(self.table_name)):
            if int(row[4]) == 0 and kronos.is_overdue(row[1], row[3]):
                rows.append(row)
        return rows

    def delete_history(self):
        self.cursor.execute("DROP TABLE {}".format(self.table_name))
        self.create_table()
        self.connection.commit()
        self.rows_in_table = 0

    def disconnect(self):
        self.connection.close()
