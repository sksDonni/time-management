import db


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


def parse_ascii_banner(file):
    f = open(file, 'r')
    lines = f.readlines()
    f.close()
    return lines


def print_ascii_banner(lines):
    for line in lines:
        print(line.rstrip("\n"))


def run_menu_loop(proxy):
    while True:
        choice = print_menu_and_get_input()
        map_user_menu_choice_to_function(choice, proxy)


def map_user_menu_choice_to_function(choice, proxy):
    if choice == "1":
        make_a_note(proxy)
    elif choice == "2":
        set_a_todo_item_with_goal(proxy)
    elif choice == "3":
        db.print_contents(proxy)
    elif choice == "4":
        complete_todo(proxy)
    elif choice == "5":
        db.get_overdue_items(proxy)
    elif choice == "6":
        delete_history_and_exit(proxy)
    elif choice == "7":
        quit_program(proxy)
    else:
        print("Choice not recognized.")


def make_a_note(proxy):
    note = input("Make a note: ")
    db.update_table_with_note(proxy, note)


def set_a_todo_item_with_goal(proxy):
    note = input("Make a TODO item: ")
    days_until_completion = input("Set number of days to complete: ")
    db.update_table_with_todo_and_goal(proxy, note, days_until_completion)


def complete_todo(proxy):
    row_id = input("Select note id for completion: ")
    db.update_completion(proxy, row_id)


def quit_program(proxy):
    print("Get outta here!")
    proxy.connection.close()
    quit()


def delete_history_and_exit(proxy):
    choice = input(
        "Are you sure you want to delete your history?\nSubmit 'y' to drop table or any other key to return the menu: ")
    if choice == "y":
        print("Deleting history...")
        db.delete_history(proxy)
