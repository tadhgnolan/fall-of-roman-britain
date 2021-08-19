
# Main game functions

def game_over(msg, function):
    """
    Game over message and function. Allows player to restart the game.
    """
    print(msg)
    print("\n GAME OVER \n")
    play_again(function)


def play_again(option):
    print("To play again type 'yes', to exit type anything else: \n")
    choice = input()
    if choice == "yes":
        option()
    else:
        print("Gratias tibi ago! (Thanks for playing!)")


def cont(prompt, opt1, path1):
    while True:
        choice = input(prompt)
        if choice == opt1:
            path1()
            break
        else:
            print(f"\nPlease enter a valid option! ({opt1}\n")
            continue

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

def three_choice_option(prompt, opt1, opt2, opt3, path1, path2, path3):
    """
    Allows input(prompt) of option(opt1,/opt2)
    with three outcomes(path1, path2, path3).
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
        elif choice == opt3:
            path3()
            break
        else:
            print(f"\nPlease enter a valid option! ({opt1}, {opt2} or {opt3}\n")
            continue
    

def four_choice_option(opt1, opt2, opt3, opt4):
    """
    Function allows for a 4 point multiple choice option.
    If input is valid, story will continue.
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

    print("##########################################################################")
    print("#                                                                        #")
    print("#                    The Fall of Roman Britain                           #")
    print("#                                                                        #")
    print("#                                               _____                    #")
    print("#     _________________________________________|     \           ____    #") 
    print("#    /                                         |     ||---------/    \   #")
    print("#  /___________________________________________|     ||        |      |  #")
    print("#  \                                           |     ||        |      |  #")
    print("#    \_________________________________________|     ||---------\____/   #")
    print("#                                              |_____/                   #")
    print("#                                                                        #")
    print("##########################################################################\n\n")


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
    print(f"\n\n Salve {PLAYER_NAME}. Alae iacta est! (Greetings {PLAYER_NAME}. The die is cast!)\n\n")
    story_intro()


# Intro/start of story.
def story_intro():

    print("It is late in the year 407AD. Constantine III has taken his army to Gaul and...\n")
    print("left Britania defenceless.\n")
    print("You are a lone Roman Centurion, the last at your fort.\n")
    print("Your Pilus Prior (commander of your cohort) has left a mission for you.\n")
    print("If within 6 months, the army does not return seek out... .\n")
    print("Flavius Sanctus in Aquae Sulis.\n")

    two_choice_option("Do you go West to Aquae Sulis or South to Durnovana? (west/south): \n",
        "west", "south", road_west, road_south)


# Western route. ******************************************************************************************************
def road_west():

    print("You take the road West, off the main Fosse Way, towards Aquae Sulis. \n")
    print("As you a approach a bend in the road you spot a lone Celtic bandit \n")

    two_choice_option("Do you attack the bandit or try to hide? (attack/hide): \n",
    "attack", "hide", attack_c_bandit, hide_c_bandit)


def attack_c_bandit():

    print("You defeat the lone bandit easily, your years of experience kicking in.\n")
    print("You continue along the road towards Aquae Sulis, noticing how... \n")
    print("the lack of available Lapidarii (stoneworkers) has left the surface... \n")
    print("of the road in a poor state. \n")
    print("Normally they would be resurfaced yearly, but it has clearly been some... \n")
    print("time since that was true.")

    cont("Type yes to continue? (yes): \n",
    "yes", as_north_gate)


def hide_c_bandit():

    print("The bandit spots you hiding below the roadside & runs you through with their spear.")

def as_north_gate():
    print("You eventually cross the River Avon and take a smaller road left... \n")
    print("to follow the river, finally seeing the walls of Aquae Sulis in the distance. \n")
    print("When you finally near the gates of the town the sun is low in the sky... \n")
    print("and you see several guards begin to light lamps. \n")
    print("There are signs of battle and fire damage fromt the outside.")
    print("You anounce yourself to the centurions guarding the gate. \n")
    as_guards()


# Town of Aquae Sulis. ************************************************************************************************ 
def as_guards():
    print("The centurion greets you in return and asks what brings you this way... \n")
    print("alone in these dangerous times. You explain you are on a mission left...")
    print("by your Pilus Prior.")

    three_choice_option("Ask what happened to the town?(town)/n\
         the townspeople? (people)/n\
         or Flavius Sanctus? (Flavius)\n",
    "town", "people", "flavius", as_town, as_people, as_flavius)


def as_town():
    print("The gua")


def as_people():
    print("people")


def as_flavius():
    print("flavius")


# Southern route. *****************************************************************************************************
def road_south():

    print("You take the road South towards Durnovana. \n")
    print("In the distance you see a large group of Saxon bandits approaching. \n")
    print("They haven't seen you yet. \n")

    two_choice_option("Do you attack the bandits or try to hide? (attack/hide): \n",
    "attack", "hide", attack_s_bandits, hide_s_bandits)


def attack_s_bandits():

    print("You attempt to surprise the bandits with an attack, but they are too many & you are... \n")
    print("overwhelmed. \n")
    game_over("You are gravely wounded and die below the roadside, mission incomplete.\n",
    start_game)

def hide_s_bandits():

    print("You successfully hide in a ditch by the roadside and the bandits pass you by. \n")


start_game()

