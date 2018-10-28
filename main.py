import interface
import db


def main():
    connection = db.create_connection()
    cursor = connection.cursor()
    db.create_table(cursor)
    interface.run_menu_loop(connection, cursor)


if __name__ == "__main__":
    main()
