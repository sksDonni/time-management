from interface_mode import run_menu_loop_mode
from facade import DatabaseFacade


def main():
    print("Welcome to Time Management!\n\n")
    database_facade = DatabaseFacade("time_management.db")
    run_menu_loop_mode(database_facade)


if __name__ == "__main__":
    main()
