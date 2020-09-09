import ddl
import sqlitedb
import unittest


class DDLTest(unittest.TestCase):
    def setUp(self) -> None:
        self.db = sqlitedb.SQLiteDatabase()
        self.data_def = ddl.DataDefinitionLanguage(self.db)
        self.data_def.create_all_tables()

    def tearDown(self) -> None:
        self.db.disconnect()

    def test_parse_json(self):
        json = ddl.DataDefinitionLanguage.parse_json(
            "time_management/table_schemas/tasks.json"
        )
        self.assertEqual("int", json.get("id"))

    def test_list_schemas(self):
        schemas = ddl.DataDefinitionLanguage.list_schemas()
        self.assertTrue("notes.json" in schemas)
        self.assertTrue("tasks.json" in schemas)
        self.assertTrue("user_config.json" in schemas)
