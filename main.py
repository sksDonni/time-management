import sqlite3
import datetime


def main():
    conn = sqlite3.connect("tm")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS tm
                    (date text, note text)''')
    note = ask()
    while note != "q":
        c.execute("INSERT INTO tm (date, note) VALUES (?, ?)", (datetime.datetime.now(), note))
        for row in c.execute("SELECT * FROM tm"):
            print(row)
        note = ask()
    conn.commit()
    conn.close()


def ask():
    return input("Note? Exit with 'q'.")


if __name__ == "__main__":
    main()
