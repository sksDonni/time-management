import interface
from facade import DatabaseFacade


def main():
    database_facade = DatabaseFacade()
    database_facade.create_table()
    interface.run_menu_loop(database_facade)


if __name__ == "__main__":
    main()
