import sqlite3
import datetime

db = "time_management.db"
table = "time_management"
schema = ["id", "date", "note", "complete_in_days", "is_complete"]


def create_table(proxy):
    proxy.cursor.execute('''CREATE TABLE IF NOT EXISTS {}
                        ({} int, {} text, {} text, {} text, {} text)'''.format(table, *schema))
    proxy.connection.commit()


def update_table_with_note(proxy, note):
    row_id = count_rows(proxy)
    row_id += 1
    proxy.cursor.execute("INSERT INTO {} ({}, {}, {}, {}, {}) VALUES (?, ?, ?, ?, ?)".format(table, *schema),
                         (row_id, datetime.datetime.now(), note, "-1", "-1"))
    proxy.connection.commit()


def update_table_with_todo_and_goal(proxy, note, completion_goal):
    row_id = count_rows(proxy)
    row_id += 1
    proxy.cursor.execute("INSERT INTO {} ({}, {}, {}, {}, {}) VALUES (?, ?, ?, ?, ?)".format(table, *schema),
                         (row_id, datetime.datetime.now(), note, completion_goal, "0"))
    proxy.connection.commit()


def update_completion(proxy, row_id):
    proxy.cursor.execute("UPDATE {} SET {} = {} WHERE id = {}".format(table, schema[4], 1, row_id))


def print_contents(proxy):
    def divide():
        return '-' * 150

    for row in proxy.cursor.execute("SELECT * FROM {}".format(table)):
        print(divide())
        print(row)
    print(divide())


def count_rows(proxy):
    return len(proxy.cursor.execute("SELECT * FROM {}".format(table)).fetchall())


def delete_history(proxy):
    proxy.cursor.execute("DROP TABLE {}".format(table))
    proxy.connection.commit()
    proxy.connection.close()
