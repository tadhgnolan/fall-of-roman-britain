

def game_over(msg, function):
    """

    """

def two_choice_option(prompt, opt1, opt2, path1, path2):
    """
    Allows input(prompt) of option(opt1,/opt2)
    with two outcomes(path1, path2).
    When user enters correct option, loop is passed
    and given path is executed.
    """
    while True:
        choice = input(prompt)
        if choice == opt1:
            path1()
            break
        elif choice == opt2:
            path2()
            break
        else:
            print(f"\nPlease enter a valid option! ({opt1} or {opt2}\n")
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
        choice = input("Which path do you choose? (1/2/3/4): \n")
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
            print("You must enter a 'number', try again\n")


def intro_msg():


    """
    Function to print welcome graphics.
    """

    print("##################################\n")
    print("#                                #\n")
    print("#   The Fall of Roman Britain    #\n")
    print("#                                #\n")
    print("##################################\n\n")


def start_game():
    """
    Starts game, retrieves username from player & welcomes them to the game.
    """

    intro_msg()

    while True:

        global PLAYER_NAME
        PLAYER_NAME = input("Please enter a name for your character: \n\n")
        if PLAYER_NAME == "":
            print("Please enter a character name to continue...\n")
            continue
        else:
            break
    print(f"Salve {PLAYER_NAME}. Alae iacta est! (Greetings {PLAYER_NAME}. The die is cast!)\n\n")
    story_intro()


def story_intro():

    print("It is the year. Constantine III has taken his army to Gaul and left Britania defenceless.\n")
    print("You are a lone Roman Centurion, the last at your fort.\n")
    print("Your Pilus Prior (commander of your cohort) has left a mission for you.\n")
    print("If within 6 months, the army does not return seek out... .\n")
    print("..Flavius Sanctus in Aquae Sulis and Lucius Septimius in Durnovana.\n")

    two_choice_option("Do you go West to Aquae Sulis or South to Durnovana? (west/south): \n",
        "west", "south", road_west, road_south)


def road_west():

    print("You take the road, known as the Fosse Way, West towards Aquae Sulis.")
    print("As you a approach a bend in the road you spot a lone Celtic bandit")

    two_choice_option("Do you attack the bandit or try to hide? (attack/hide): \n",
    "attack", "hide", attack_c_bandit, hide_c_bandit)


def road_south():

    print("You take the road South towards Durnovana.")
    print("In the distance you see a large group of Saxon bandits approaching.")
    print("They haven't seen you yet.")

    two_choice_option("Do you attack the bandits or try to hide? (attack/hide): \n",
    "attack", "hide", attack_s_bandits, hide_s_bandits)


def attack_c_bandit():

    print("You defeat the lone bandit easily, your years of experience kickin in")
    print("You continue along the road towards Aquae Sulis, noticing how")
    print("...the lack of available Lapidarii (stoneworkers) has left the surface")
    print("...of the road in a poor state.")
    print("Normally they would be resurfaced yearly, but it has clearly been some")
    print("time since that was true.")

    two_choice_option("Continue to Aquae Sulis? (continue): \n",
    "continue", "continue", approach_aquae_sulis, approach_aquae_sulis)


def hide_c_bandit():

    print("The bandit spots you hiding below the roadside & runs you through with their spear")

def approach_aquae_sulis():
    print("You eventually cross the River Avon and take a smaller road left")
    print("to follow it, finally seeing the walls of Aquae Sulis in the distance.")
    print("When you finally near the gates of the town the sun is low in the sky")
    print("and you see several guards begin to light lamps.")
    print("You anounce yourself to the centurions guarding the gate.")

def attack_s_bandits():

    print("You attempt to surprise the bandits with an attack, but they are too many & you are")
    print("overwhelmed.")


def hide_s_bandits():

    print("You successfully hide in a ditch by the roadside and the bandits pass you by.")


start_game()

