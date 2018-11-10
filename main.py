import interface
from proxy import DatabaseProxy


def main():
    proxy = DatabaseProxy()
    proxy.create_table()
    interface.run_menu_loop(proxy)


if __name__ == "__main__":
    main()
