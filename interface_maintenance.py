from interface_common import (
    parse_ascii_banner,
    print_ascii_banner,
    clear_screen,
    quit_program,
)


def prompt_maintenance():
    print_ascii_banner(parse_ascii_banner("banners/maintenance.txt"))
    return input(
        """
1: Delete history
2: Quit
"""
    )


def run_menu_loop_maintenance(facade):
    while True:
        choice = prompt_maintenance()
        clear_screen()
        map_choice_to_function(choice, facade)


def map_choice_to_function(choice, facade):
    if choice == "1":
        delete_history(facade)
    elif choice == "2":
        quit_program(facade)
    else:
        print("Choice not recognized.")


def delete_history(facade):
    clear_screen()
    choice = input(
        "Are you sure you want to delete your history?\nSubmit 'y' to drop table or any other key to return the menu: "
    )
    if choice == "y":
        print("Deleting history...")
        facade.delete_history()
