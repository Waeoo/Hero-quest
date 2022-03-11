import os


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def run_game():
    clear()
    print("Welcome to Hero Quest")


run_game()
