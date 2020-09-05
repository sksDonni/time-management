import ddl
import unittest


class DDLTest(unittest.TestCase):
    def setUp(self) -> None:
        self.__database = ddl.Database()
        self.data_def = ddl.DataDefinitionLanguage(self.__database)
        self.table_name = "test"
        self.schema = ddl.parse_json("time_management/table_schemas/notes.json")

    def tearDown(self) -> None:
        self.__database.disconnect()

    def test_parse_json(self):
        json = ddl.parse_json("time_management/table_schemas/notes.json")
        self.assertEqual("text", json.get("note"))

    def test_database(self):
        self.assertEqual(":memory:", self.__database.get_db_name())

    def test_create_sql(self):
        self.assertEqual(
            "CREATE TABLE IF NOT EXISTS test ('id' 'int', 'type' 'text', 'date' 'text', 'note' 'text')",
            self.data_def.create_sql(self.table_name, self.schema),
        )

    def test_create_table(self):
        self.data_def.create_table(self.table_name, self.schema)
