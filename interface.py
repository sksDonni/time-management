def print_menu_and_get_input():
    print_ascii_banner(parse_ascii_banner("banner.txt"))
    return input('''
1: Make a note.
2: Make a TODO item and set a completion goal.
3: Print your notes and TODOs.
4: Complete a TODO.
5: Print overdue TODOs.
6: Delete your time management history.
7: Quit.
''')


def divide():
    return '-' * 150


def parse_ascii_banner(file):
    f = open(file, 'r')
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
        delete_history(facade)
    elif choice == "7":
        quit_program(facade)
    else:
        print("Choice not recognized.")


def make_a_note(facade):
    note = input("Make a note: ")
    facade.update_table_with_note(note)


def set_a_todo_item_with_goal(facade):
    note = input("Make a TODO item: ")
    days_until_completion = input("Set number of days to complete: ")
    facade.update_table_with_todo_and_goal(note, days_until_completion)


def print_contents(facade):
    table_rows = facade.get_all_items()
    for row in table_rows:
        print(divide())
        print(row)
    print(divide())


def complete_todo(facade):
    row_id = input("Select note id for completion: ")
    facade.update_completion(row_id)


def print_overdue_items(facade):
    table_rows = facade.get_overdue_items()
    for row in table_rows:
        print(divide())
        print(row)
    print(divide())


def delete_history(facade):
    choice = input(
        "Are you sure you want to delete your history?\nSubmit 'y' to drop table or any other key to return the menu: ")
    if choice == "y":
        print("Deleting history...")
        facade.delete_history()


def quit_program(facade):
    print("Get outta here!")
    facade.disconnect()
    quit()
