from interface_common import (
    parse_ascii_banner,
    print_ascii_banner,
    quit_program,
    clear_screen,
)
from interface_time_management import run_menu_loop_tm
from interface_maintenance import run_menu_loop_maintenance


def prompt_mode():
    clear_screen()
    print_ascii_banner(parse_ascii_banner("banners/mode.txt"))
    return input(
        """
1: Time management
2: Analytics
3: Maintenance
4: Quit
"""
    )


def map_choice_to_function(choice, facade):
    if choice == "1":
        clear_screen()
        run_menu_loop_tm(facade)
    elif choice == "2":
        pass
    elif choice == "3":
        clear_screen()
        run_menu_loop_maintenance(facade)
    elif choice == "4":
        quit_program(facade)
    else:
        print("Choice not recognized.")


def run_menu_loop_mode(facade):
    while True:
        choice = prompt_mode()
        map_choice_to_function(choice, facade)
