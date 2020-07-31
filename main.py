from interface_mode import run_menu_loop_mode
from facade import DatabaseFacade


def main():
    database_facade = DatabaseFacade()
    run_menu_loop_mode(database_facade)


if __name__ == "__main__":
    main()
