import termcolor
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

    termcolor.cprint("##########################################################################", 'green')
    termcolor.cprint("#                                                                        #", 'green')
    termcolor.cprint("#                    The Fall of Roman Britain                           #", 'green')
    termcolor.cprint("#                                                                        #", 'green')
    termcolor.cprint("#                                               _____                    #", 'green')
    termcolor.cprint("#     _________________________________________|     \           ____    #", 'green') 
    termcolor.cprint("#    /                                         |     ||---------/    \   #", 'green')
    termcolor.cprint("#  /___________________________________________|     ||        |      |  #", 'green')
    termcolor.cprint("#  \                                           |     ||        |      |  #", 'green')
    termcolor.cprint("#    \_________________________________________|     ||---------\____/   #", 'green')
    termcolor.cprint("#                                              |_____/                   #", 'green')
    termcolor.cprint("#                                                                        #", 'green')
    termcolor.cprint("#                          By Tadhg Nolan                                #", 'green')
    termcolor.cprint("##########################################################################\n\n", 'green')


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

    termcolor.cprint("It is late in the year 407 AD. Constantine III has taken his army to Gaul...\n", 'green')
    print("and left Britannia defenceless.\n")
    print("You are a lone Roman Centurion, the last at your fort.\n")
    print("Your Pilus Prior (commander of your cohort) has left a mission for you.\n")
    print("If within 6 months, the army does not return seek out... .\n")
    print("Flavius Sanctus in Aquae Sulis.\n")

    two_choice_option("Do you go West to Aquae Sulis or South to Durnovana? (west/south): \n",
        "west", "south", road_west, road_south)


# Western route. ******************************************************************************************************
def road_west():

    print("\nYou take the road West, off the main Fosse Way, towards Aquae Sulis. \n")
    print("As you a approach a bend in the road you spot a lone Celtic bandit \n")

    two_choice_option("Do you attack the bandit or try to hide? (attack/hide): \n",
    "attack", "hide", attack_c_bandit, hide_c_bandit)


def attack_c_bandit():

    print("\nYou defeat the lone bandit easily, your years of experience\n\
        kicking in.\n")
    print("You continue along the road towards Aquae Sulis, noticing\n\
        how...\n")
    print("the lack of available Lapidarii (stoneworkers) has left the\n\
        surface...\n")
    print("of the road in a poor state. \n")
    print("Normally they would be resurfaced yearly, but it has clearly\n\
        been some... \n")
    print("time since that was true.")

    cont("Type cont to continue. (cont):\n",
    "cont", as_north_gate)


def hide_c_bandit():

    print("The bandit spots you hiding below the roadside & runs you\n\
        through with their spear.")

def as_north_gate():
    print("\nYou eventually cross the River Avon and take a smaller\n\
        road left... \n")
    print("to follow the river, finally seeing the walls of Aquae Sulis\n\
        in the distance. \n")
    print("When you finally near the gates of the town the sun is low\n\
        in the sky... \n")
    print("and you see several guards begin to light lamps. \n")
    print("There are signs of battle and fire damage fromt the outside.")
    print("You anounce yourself to the centurions guarding the gate. \n")
    as_guards()


# Town of Aquae Sulis. ****************************************************** 
def as_guards():
    print("\nThe centurion greets you in return and asks what brings you\n\
         this way... \n")
    print("alone in these dangerous times. You explain you are on a\n\
         mission left...")
    print("by your Pilus Prior.\n")

    three_choice_option("Ask what happened to the town?(town)\n\
         the townspeople? (people)\n\
         or Flavius Sanctus? (flavius)\n",
        "town", "people", "flavius", as_town, as_people, as_flavius)


def as_town():
    print("The guard tells you that the frequent attacks from the Celtae\n\
        and the lack of skilled workmen has left the town in a bad state.\n")
    print("Looking around the town you see collapsed rooves and\n\
        burnt, crumbling walls of several buildings.")

    two_choice_option("Ask what happened to the townspeople? (people)\n\
        or Flavius Sanctus? (flavius)\n",
        "people", "flavius", as_people, as_flavius) 


def as_people():
    print("The guard tells you most of the citizens have left the town due to...\n\
        constant raids by Celtae tribes from Hibernia.")
        
    two_choice_option("Ask what happened to the town?(town)\n\
        or Flavius Sanctus? (flavius)\n",
        "town", "flavius", as_town, as_flavius)


def as_flavius():
    print("The guard tells you the Governor Flavius Sanctus is in the basilica with...\n\
        members of the cohort.")

    three_choice_option("Take the avenue to the centre of the town? (avenue),\n\
        ask about the townspeople? (people)\n\
        or ask about the town? (town)\n",
        "avenue", "people", "town", as_avenue, as_people, as_town)


def as_avenue():
    print("Like most Roman towns, there are two main avenues,")
    print("the one you are on runs North to South and at the center...")
    print("of the town it meets the other which runs East to West.")
    print("As you approach the town centre, you can see the temple and...")
    print("amphitheatre nearest to you, then the baths, forum and basilica...")
    print("behind them.")

    three_choice_option("Explore the temple? (temple),\n\
        explore the amphitheatre? (theatre)\n\
        or continue to the baths, forum and basilica? (bath)\n",
        "temple", "theatre", "bath", as_temple, as_theatre, as_bath)


def as_temple():
    print("You walk towards the modest square, wooden temple, dedicated to the godess Sulis Minerva.\n")
    print("As you enter through the front, you notice members of the godess's cult making offerings...\n")
    print("to her statue, enshrined on an alter at the rounded back of the temple.\n")

    two_choice_option("Explore the theatre? (theatre)\n\
        or continue to the baths, forum and basilica? (bath)\n",
        "theatre", "bath", as_theatre, as_bath)


def as_theatre():
    print("As you approach the amphitheatre you notice all of the wooden benches have been...\n")
    print("either broken or burned, leaving behind the stone steps underneath.\n")
    print("Some of the masonry has started to crumble as well. It is a shadow of its former self.")

    two_choice_option("Explore the temple? (temple)\n\
        or continue to the baths, forum and basilica? (bath)\n",
        "temple", "bath", as_temple, as_bath)

def as_bath():
    print("You walk further along the East-West avenue, towards the baths, forum and basilica\n")

    three_choice_option("Explore the baths? (thermae),\n\
        the forum? (forum)\n\
        or the basilica? (basilica)\n",
        "thermae", "forum", "basilica", as_thermae, as_forum, as_basilica)


def as_thermae():
    print("The baths are a large complex of stone buildings, split up into naturally....\n")
    print("& furnace heated baths of differing temperatures as well as sweat rooms.\n")
    print("It seems to be well maintained, despite the state of the rest of the town...\n")
    print("and you can hear that the furnaces are still being operated.\n")
    print("If you had more time, you would like to enjoy their use.\n")

    two_choice_option("Explore the forum? (forum)\n\
        or the basilica? (basilica)\n",
        "forum", "basilica", as_forum, as_basilica)


def as_forum():
    print("You approach the forum, a large open rectangular space surrounded by columns.\n")
    print("It is normally the site of all the towns major social, political and...\n")
    print("religious gatherings and festivals, but there are signs it hasn't...\n")
    print("been used in a some time. Debris and animal excrement litter the cobbles.\n")
    
    two_choice_option("Explore the baths? (thermae) or the basilica? (basilica)\n",
       "thermae", "basilica", as_thermae, as_basilica)


def as_basilica():
    print("The basilica is a large rectangular stone building with a vaulted...\n")
    print("roof, very similar in layout to a modern church. It serves the purpose...\n")
    print("of court house, administrative center as well as many other functions.\n")
    print("There are many members of a cohort standing gathered all around the interior.\n")
    print("At the far end you spot Flavius Sanctus speaking to members of the cohort.\n")

    cont("Type cont to continue. (cont):\n",
    "cont", the_mission)


def the_mission():
    print("As you approach, Flavius turns towards you and says...\n")
    print(f"'Ah {PLAYER_NAME}. Welcome. Right on time, just as Gnaeus Calvinus...\n")
    print("said you would be.' This takes you aback somewhat. As far as...\n")
    print("you were aware, this was just a contingency plan.\n")
    print("Snapping back to attention and realising who you're speaking to,\n")
    print("you ask 'How may I be of service.\n")

    cont("Type cont to continue. (cont):\n",
    "cont", the_mission_2)


def the_mission_2():
    print("'Straight to business, eh?' He chuckles wryly.\n")
    print("As you are aware, the situation is not good for Britannia.\n")
    print("Contact with Rome has become more and more sparse...\n")
    print("and we have precious few defenders left.\n")
    print("I need you to bring this scroll to Lucius Septimius...\n")
    print("in Durnovana as quickly as possible.\n")

    cont("Type cont to continue. (cont):\n",
    "cont", the_mission_3)


def the_mission_3():
    print("the mission 3")



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

