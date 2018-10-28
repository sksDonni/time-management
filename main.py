import interface
import db
from proxy import DbProxy


def main():
    proxy = DbProxy("time-management.db")
    db.create_table(proxy)
    interface.run_menu_loop(proxy)


if __name__ == "__main__":
    main()
