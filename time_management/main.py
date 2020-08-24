from interface_mode import run_menu_loop_mode
from facade import DatabaseFacade
from kronos import get_time_of_day
import os
import getpass


def main():
    database = os.path.join(os.path.dirname(__file__), "time_management.db")
    database_facade = DatabaseFacade(database)
    on_startup(database_facade)
    run_menu_loop_mode(database_facade)


def on_startup(facade):
    time_of_day = get_time_of_day()
    user = getpass.getuser()
    number_of_overdue_items = len(facade.get_overdue_items())
    welcome_statement = (
        f"Good {time_of_day} {user}. You have {number_of_overdue_items} overdue items."
    )
    print(2 * "\n")
    print(welcome_statement)
    print(2 * "\n")


if __name__ == "__main__":
    main()
