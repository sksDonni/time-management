from interface_common import (
    parse_ascii_banner,
    print_ascii_banner,
    clear_screen,
    quit_program,
    to_previous_menu,
)
import os


def prompt_analytics():
    banner = os.path.join(os.path.dirname(__file__), "banners/lytics.txt")
    print_ascii_banner(parse_ascii_banner(banner))
    return input(
        """
0: Return to MODE
1: Print metrics
2: Quit
"""
    )


def run_menu_loop_analytics(facade):
    while True:
        choice = prompt_analytics()
        map_choice_to_function(choice, facade)


def map_choice_to_function(choice, facade):
    if choice == "0":
        to_previous_menu(facade)
    elif choice == "1":
        clear_screen()
        pass
    elif choice == "2":
        quit_program(facade)
    else:
        print("Choice not recognized.")
