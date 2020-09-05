import interface_common
import interface_time_management
import interface_maintenance
import interface_analytics
import os


def prompt_mode():
    interface_common.initialize_menu(run_menu_loop_mode, True)
    banner = os.path.join(os.path.dirname(__file__), "banners/mode.txt")
    interface_common.print_ascii_banner(interface_common.parse_ascii_banner(banner))
    return input(
        """
1: Time management
2: Analytics
3: Maintenance
4: Quit
"""
    )


def map_choice_to_function(choice, facade):
    if choice == "1":
        interface_common.initialize_menu(interface_time_management.run_menu_loop_tm)
        interface_time_management.run_menu_loop_tm(facade)
    elif choice == "2":
        interface_common.initialize_menu(interface_analytics.run_menu_loop_analytics)
        interface_analytics.run_menu_loop_analytics(facade)
    elif choice == "3":
        interface_common.initialize_menu(
            interface_maintenance.run_menu_loop_maintenance
        )
        interface_maintenance.run_menu_loop_maintenance(facade)
    elif choice == "4":
        interface_common.quit_program(facade)
    else:
        print("Choice not recognized.")


def run_menu_loop_mode(facade):
    while True:
        choice = prompt_mode()
        map_choice_to_function(choice, facade)
