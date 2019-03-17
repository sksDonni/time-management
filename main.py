import interface
from proxy import DatabaseFacade


def main():
    proxy = DatabaseFacade()
    proxy.create_table()
    interface.run_menu_loop(proxy)


if __name__ == "__main__":
    main()
