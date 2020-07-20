from os import system, name


def print_menu_and_get_input():
    print_ascii_banner(parse_ascii_banner("banner.txt"))
    return input(
        """
1: Make a note.
2: Make a TODO item and set a completion goal.
3: Print your notes and TODOs.
4: Complete a TODO.
5: Print overdue TODOs.
6: Print SCRUM notes.
7: Delete your time management history.
8: Quit.
"""
    )


def parse_ascii_banner(file):
    f = open(file, "r")
    lines = f.readlines()
    f.close()
    return lines


def print_ascii_banner(lines):
    for line in lines:
        print(line.rstrip("\n"))


def run_menu_loop(facade):
    while True:
        choice = print_menu_and_get_input()
        map_user_menu_choice_to_function(choice, facade)


def map_user_menu_choice_to_function(choice, facade):
    if choice == "1":
        make_a_note(facade)
    elif choice == "2":
        set_a_todo_item_with_goal(facade)
    elif choice == "3":
        print_contents(facade)
    elif choice == "4":
        complete_todo(facade)
    elif choice == "5":
        print_overdue_items(facade)
    elif choice == "6":
        print_scrum_notes(facade)
    elif choice == "7":
        delete_history(facade)
    elif choice == "8":
        quit_program(facade)
    else:
        print("Choice not recognized.")


def make_a_note(facade):
    clear_screen()
    note = input("Make a note: ")
    facade.update_table_with_note(note)
    clear_screen()


def set_a_todo_item_with_goal(facade):
    clear_screen()
    note = input("Make a TODO item: ")
    days_until_completion = input("Set number of days to complete: ")
    facade.update_table_with_todo_and_goal(note, days_until_completion)
    clear_screen()


def print_contents(facade):
    clear_screen()
    table_rows = facade.get_all_items()
    for row in table_rows:
        print(row)
    print("\n\n")


def clear_screen():
    if name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")


def complete_todo(facade):
    clear_screen()
    row_id = input("Select note id for completion: ")
    facade.update_completion(row_id)
    clear_screen()


def print_overdue_items(facade):
    clear_screen()
    table_rows = facade.get_overdue_items()
    for row in table_rows:
        print(row)


def print_scrum_notes(facade):
    clear_screen()
    print_ascii_banner(parse_ascii_banner("SCRUM.txt"))
    table_rows = facade.get_last_days_items()
    for row in table_rows:
        print(row)


def delete_history(facade):
    clear_screen()
    choice = input(
        "Are you sure you want to delete your history?\nSubmit 'y' to drop table or any other key to return the menu: "
    )
    if choice == "y":
        print("Deleting history...")
        facade.delete_history()
    clear_screen()


def quit_program(facade):
    print("Get outta here!")
    facade.disconnect()
    quit()
