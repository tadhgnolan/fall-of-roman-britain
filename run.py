import sys
import time


def typing(text, speed):
    """
    Modified print function. Introduces timing in-between characters.
    text = The text you wish to print.
    speed = Adjusts the timing in-between characters.
    """
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)


def two_choice_option(prompt, opt1, opt2, path1, path2):
    """
    Allows input(prompt) of option(opt1,/opt2)
    with two outcomes(path1, path2).
    When user enters correct option, loop is passed
    and given path is executed.
    """
    while True:
        choice =input(prompt)
        if choice == opt1:
            path1()
            break
        elif choice == opt2:
            path2()
            break
        else:
            print()
            print(f"Please enter a valid option! ({opt1} or {opt2}\n")
            continue


def four_choice_option(opt1, opt2, opt3, opt4):
    """
    Function allows for a 4 point multiple choice option,
    if input is valid, story will continue.
    If input is not an integer, it will throw a ValueError
    and prompt for input again. If the input is an integer but is not
    valid, it will ask for input again
    """
    while True:
        choice = input ("Which path do you choose? (1/2/3/4): \n")
        try:
            input_int = int(choice)
            if input_int == 1:
                opt1()
                break
            elif input_int == 2:
                opt2()
                break
            elif input_int == 3:
                opt3()
                break
            elif input_int == 4:
                opt4()
                break
            else:
                print("Please enter correct option (1/2/3/4.")
                continue
        except ValueError:
            print("You must enter a 'number', try again")


def intro_msg():


    """
    Function to print welcome graphics.
    """

    print()
    typing("##################################\n", 0.01)
    typing("#                                #\n", 0.01)
    typing("#   The Fall of Roman Britain    #\n", 0.01)
    typing("#                                #\n", 0.01)
    typing("##################################\n\n", 0.01)



def start_game():
    """
    Starts game, retrieves username from player & welcomes them to the game.
    """

    intro_msg()


    while True:

        global PLAYER_NAME
        PLAYER_NAME = input("Please enter a name for your character: \n")
        print()
        if PLAYER_NAME == "":
            print("Please enter a character name to continue...\n")
            continue
        else:
            break
    typing(f"Salve {PLAYER_NAME}. Alae iacta est! (Greetings {PLAYER_NAME}. The die is cast!\n\n", 0.03)
    option_one()
