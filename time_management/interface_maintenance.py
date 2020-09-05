import interface_common
import os


def prompt_maintenance():
    banner = os.path.join(os.path.dirname(__file__), "banners/maint.txt")
    interface_common.print_ascii_banner(interface_common.parse_ascii_banner(banner))
    return input(
        """
0: Return to MODE
1: Delete history
2: Quit
"""
    )


def run_menu_loop_maintenance(facade):
    while True:
        choice = prompt_maintenance()
        map_choice_to_function(choice, facade)


def map_choice_to_function(choice, facade):
    if choice == "0":
        interface_common.to_previous_menu(facade)
    elif choice == "1":
        delete_history(facade)
    elif choice == "2":
        interface_common.quit_program(facade)
    else:
        print("Choice not recognized.")


def delete_history(facade):
    interface_common.clear_screen()
    choice = input(
        "Are you sure you want to delete your history?\nSubmit 'y' to drop table\nSubmit 'n' to return to maintenance\n"
    )
    if choice == "y":
        print("\nDeleting history...\n\n")
        facade.delete_history()
    elif choice == "n":
        run_menu_loop_maintenance(facade)
