import interface_mode
import facade
import kronos
import os
import getpass
import ddl
import sqlitedb


def main():
    # Deprecated
    # ---------------------------------------------------------------------
    database = os.path.join(os.path.dirname(__file__), "time_management.db")
    database_facade = facade.DatabaseFacade(database)
    # ---------------------------------------------------------------------

    db_v2 = sqlitedb.SQLiteDatabase(os.path.join(os.path.dirname(__file__), "TM.db"))
    data_def = ddl.DataDefinitionLanguage(db_v2)
    data_def.create_all_tables()

    on_startup(database_facade)
    interface_mode.run_menu_loop_mode(database_facade)


def on_startup(facade):
    time_of_day = kronos.get_time_of_day()
    user = getpass.getuser()
    number_of_overdue_items = len(facade.get_overdue_items())
    welcome_statement = f"\nGood {time_of_day} {user}. You have {number_of_overdue_items} overdue items.\n"
    print(welcome_statement)


if __name__ == "__main__":
    main()
