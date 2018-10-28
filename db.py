import sqlite3
import datetime

db = "time_management.db"
table = "time_management"
schema = ["date", "note", "complete_in_days", "is_complete"]


def create_connection():
    return sqlite3.connect(db)


def create_table(cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS {}
                        ({} text, {} text, {} text, {} text)'''.format(table, *schema))


def update_table_with_note(cursor, note):
    cursor.execute("INSERT INTO {} ({}, {}, {}, {}) VALUES (?, ?, ?, ?)".format(table, *schema),
                   (datetime.datetime.now(), note, "-1", "-1"))


def update_table_with_todo_and_goal(cursor, note, completion_goal):
    cursor.execute("INSERT INTO {} ({}, {}, {}, {}) VALUES (?, ?, ?, ?)".format(table, *schema),
                   (datetime.datetime.now(), note, completion_goal, "0"))


def print_contents(cursor):
    def divide():
        return '-' * 150

    for row in cursor.execute("SELECT * FROM {}".format(table)):
        print(divide())
        print(row)
    print(divide())


def delete_history(cursor):
    cursor.execute("DROP TABLE {}".format(table))
