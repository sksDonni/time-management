from os import system, name


def parse_ascii_banner(file):
    f = open(file, "r")
    lines = f.readlines()
    f.close()
    return lines


def print_ascii_banner(lines):
    for line in lines:
        print(line.rstrip("\n"))
    print("\n")


def clear_screen():
    if name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")


def quit_program(facade):
    print("Get outta here!")
    facade.disconnect()
    quit()
