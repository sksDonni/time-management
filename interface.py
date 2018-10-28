import db


def print_menu_and_get_input():
    return input(''' {}
1: Make a note.
2: Make a TODO item and set a completion goal.
3: Print your notes and TODOs.
4: Delete your time management history.
5: Quit.
'''.format('*' * 65 + "  Time Management  " + '*' * 65))


def run_menu_loop(connection, cursor):
    while True:
        choice = print_menu_and_get_input()
        map_user_menu_choice_to_function(choice, connection, cursor)


def map_user_menu_choice_to_function(choice, connection, cursor):
    if choice == "1":
        make_a_note(cursor)
        connection.commit()
    elif choice == "2":
        set_a_todo_item_with_goal(cursor)
        connection.commit()
    elif choice == "3":
        db.print_contents(cursor)
    elif choice == "4":
        delete_history_and_exit(cursor, connection)
    elif choice == "5":
        quit_program(connection)
    else:
        print("Choice not recognized.")


def make_a_note(cursor):
    note = input("Make a note: ")
    db.update_table_with_note(cursor, note)


def set_a_todo_item_with_goal(cursor):
    goal = input("Make a TODO item: ")
    days_until_completion = input("Set number of days to complete: ")
    db.update_table_with_todo_and_goal(cursor, days_until_completion, goal)


def quit_program(connection):
    print("Get outta here!")
    connection.close()
    quit()


def delete_history_and_exit(cursor, connection):
    print("Dropping table and exiting program. Goodbye!")
    db.delete_history(cursor)
    connection.commit()
    connection.close()
    quit()
