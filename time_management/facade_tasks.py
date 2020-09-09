import logging
import ddl
import dml
import kronos
import facade_abc


class TasksFacade(facade_abc.AbcFacade):
    def __init__(self, database):
        self.db = database
        self.ddl = ddl.DataDefinitionLanguage(database)
        self.dml = dml.DataManipulationLanguage(database)
        self.table_name = "tasks"
        self.rows_in_table = 0
        try:
            self.schema = ddl.DataDefinitionLanguage.parse_json(
                "time_management/table_schemas/" + self.table_name + ".json"
            )
        except ValueError:
            logging.error("Unable to parse schema")

    def count_rows(self):
        return len(self.get_rows())

    def get_rows(self):
        return self.dml.select_star_sql(self.table_name)

    def delete_history(self):
        self.ddl.drop_table(self.table_name)

    def disconnect(self):
        self.db.disconnect()

    def get_ids(self):
        ids = []
        for row in self.get_rows():
            ids.append(row[0])
        return ids

    def complete_task(self, row_id):
        now = kronos.get_date_time_as_string()
        self.db.get_cursor().execute(
            f"UPDATE {self.table_name} SET is_complete = 'true', date_complete = '{now}' WHERE id = {row_id}"
        )
        self.db.get_connection().commit()

    def get_overdue_tasks(self):
        rows = []
        for row in self.get_rows():
            date_set = row[2]
            complete_in_days = row[4]
            is_complete = row[6]
            if is_complete == "false":
                if kronos.is_overdue(date_set, complete_in_days):
                    rows.append(row)
        return rows

    def update_table_with_task(self, task, completion_goal):
        self.rows_in_table = self.rows_in_table + 1
        self.db.get_cursor().execute(
            "INSERT INTO {} ({}, {}, {}, {}, {}, {}, {}, {}) VALUES (?, ?, ?, ?, ?, ?, ?, ?)".format(
                self.table_name, *self.schema
            ),
            (
                self.rows_in_table,
                "TASK",
                kronos.get_date_time_as_string(),
                task,
                completion_goal,
                "NULL",
                "false",
                "false",
            ),
        )
        self.db.get_connection().commit()
