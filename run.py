import os

# count steps taken
STEPS = 0


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def run_game():
    clear()
    print("Welcome to Hero Quest")


def move_left():
    clear()
    steps_check()


def move_right():
    clear()
    steps_check()


def move_forward():
    clear()
    steps_check()


def steps_check():
    if not STEPS <= 10:
        end_game()


def end_game():
    pass


run_game()
