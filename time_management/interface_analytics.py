import interface_common
import os


def prompt_analytics():
    banner = os.path.join(os.path.dirname(__file__), "banners/lytics.txt")
    interface_common.print_ascii_banner(interface_common.parse_ascii_banner(banner))
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
        interface_common.to_previous_menu(facade)
    elif choice == "1":
        interface_common.clear_screen()
        pass
    elif choice == "2":
        interface_common.quit_program(facade)
    else:
        print("Choice not recognized.")
