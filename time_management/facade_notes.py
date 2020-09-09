import logging
import ddl
import dml
import kronos
import facade_abc


class NotesFacade(facade_abc.AbcFacade):
    def __init__(self, database):
        self.db = database
        self.ddl = ddl.DataDefinitionLanguage(database)
        self.dml = dml.DataManipulationLanguage(database)
        self.table_name = "notes"
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

    def update_table_with_note(self, note):
        self.rows_in_table = self.rows_in_table + 1
        self.db.get_connection().execute(
            "INSERT INTO {} ({}, {}, {}, {}) VALUES (?, ?, ?, ?)".format(
                self.table_name, *self.schema
            ),
            (self.rows_in_table, "NOTE", kronos.get_date_time_as_string(), note),
        )
        self.db.get_connection().commit()
