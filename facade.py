import sqlite3
import kronos


class DatabaseFacade:
    rows_in_table = 0
    database_name = "time_management.db"
    table_name = "time_management"
    schema = {
        "id": "id",
        "date": "date",
        "note": "note",
        "complete_in_days": "complete_in_days",
        "is_complete": "is_complete",
    }

    # noinspection PyBroadException
    def __init__(self):
        self.connection = sqlite3.connect(self.database_name)
        self.cursor = self.connection.cursor()
        try:
            self.rows_in_table = self.count_rows()
            print("Welcome to Time Management!\n\n")
        except ValueError:
            print("Cannot read from database")

    def create_table(self):
        self.cursor.execute(
            """CREATE TABLE IF NOT EXISTS {}
                            ({} int, {} text, {} text, {} text, {} text)""".format(
                self.table_name, *self.schema
            )
        )
        self.connection.commit()

    def update_table_with_note(self, note):
        self.rows_in_table = self.rows_in_table + 1
        self.cursor.execute(
            "INSERT INTO {} ({}, {}, {}, {}, {}) VALUES (?, ?, ?, ?, ?)".format(
                self.table_name, *self.schema
            ),
            (self.rows_in_table, kronos.get_date_time_as_string(), note, "-1", "-1"),
        )
        self.connection.commit()

    def count_rows(self):
        return len(
            self.cursor.execute("SELECT * FROM {}".format(self.table_name)).fetchall()
        )

    def update_table_with_todo_and_goal(self, note, completion_goal):
        self.rows_in_table = self.rows_in_table + 1
        self.cursor.execute(
            "INSERT INTO {} ({}, {}, {}, {}, {}) VALUES (?, ?, ?, ?, ?)".format(
                self.table_name, *self.schema
            ),
            (
                self.rows_in_table,
                kronos.get_date_time_as_string(),
                note,
                completion_goal,
                "0",
            ),
        )
        self.connection.commit()

    def update_completion(self, row_id):
        self.cursor.execute(
            "UPDATE {} SET {} = {} WHERE id = {}".format(
                self.table_name, self.schema["is_complete"], 1, row_id
            )
        )

    def get_all_items(self):
        rows = []
        for row in self.cursor.execute("SELECT * FROM {}".format(self.table_name)):

            item_no = row[0]
            date = row[1]
            note = row[2]
            days_to_complete = row[3]
            is_complete = row[4]

            if days_to_complete == "-1":
                days_to_complete = "NA"
                is_complete = "NA"
            elif is_complete == "0":
                is_complete = "false"
            else:
                is_complete = "true"

            item = f"Item No: {item_no}, Date: {date}, Note: {note}, Days to complete: {days_to_complete}, Completed: {is_complete}"
            rows.append(item)
        return rows

    def get_overdue_items(self):
        rows = []
        for row in self.cursor.execute("SELECT * FROM {}".format(self.table_name)):
            item_no = row[0]
            date = row[1]
            note = row[2]
            days_to_complete = row[3]
            is_complete = row[4]
            if int(is_complete) == 0 and kronos.is_overdue(date, days_to_complete):
                item = f"Item No: {item_no}, Date: {date}, Note: {note}, Days to complete: {days_to_complete}, Completed: {is_complete}"
                rows.append(item)
        return rows

    # TODO :: HANDLE MONDAY
    def get_last_days_items(self):
        rows = []
        for row in self.cursor.execute("SELECT * FROM {}".format(self.table_name)):
            item_no = row[0]
            date = row[1]
            note = row[2]
            days_to_complete = row[3]
            is_complete = row[4]
            if kronos.is_yesterday(date):
                item = f"Item No: {item_no}, Date: {date}, Note: {note}, Days to complete: {days_to_complete}, Completed: {is_complete}"
                rows.append(item)
        return rows

    def delete_history(self):
        self.cursor.execute("DROP TABLE {}".format(self.table_name))
        self.create_table()
        self.connection.commit()
        self.rows_in_table = 0

    def disconnect(self):
        self.connection.close()
