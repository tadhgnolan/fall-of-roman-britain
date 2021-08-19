import termcolor
# Main game functions


def game_over(msg, function):
    """
    Game over message and function. Allows player to restart the game.
    """
    print(msg)
    print("\n GAME OVER \n")
    play_again(function)


def game_win(msg, function):
    print(msg)
    print("Congratulations on completing Fall of Roman Britain.\n")
    print("I hope you enjoyed your time in the 5th Century.\n")
    print("More adventures await!\n")
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
            print(f"\nPlease enter a valid option! \n\
            ({opt1}, {opt2} or {opt3}\n")
            continue


def intro_msg():
    """
    Function to print welcome graphics.
    """
    termcolor.cprint(
        "##########################################################################", 'green')
    termcolor.cprint(
        "#                                                                        #", 'green')
    termcolor.cprint(
        "#                    The Fall of Roman Britain                           #", 'green')
    termcolor.cprint(
        "#                                                                        #", 'green')
    termcolor.cprint(
        "#                                               _____                    #", 'green')
    termcolor.cprint(
        "#     _________________________________________|     \           ____    #", 'green')
    termcolor.cprint(
        "#    /                                         |     ||---------/    \   #", 'green')
    termcolor.cprint(
        "#  /___________________________________________|     ||        |      |  #", 'green')
    termcolor.cprint(
        "#  \                                           |     ||        |      |  #", 'green')
    termcolor.cprint(
        "#    \_________________________________________|     ||---------\____/   #", 'green')
    termcolor.cprint(
        "#                                              |_____/                   #", 'green')
    termcolor.cprint(
        "#                                                                        #", 'green')
    termcolor.cprint(
        "#                          By Tadhg Nolan                                #", 'green')
    termcolor.cprint(
        "##########################################################################\n\n", 'green')


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
    print(f"\n\n Salve {PLAYER_NAME}. Alae iacta est! \n\
    (Greetings {PLAYER_NAME}. The die is cast!)\n\n")
    story_intro()


# Intro/start of story.
def story_intro():

    termcolor.cprint("It is late in the year 407 AD\n", 'green')
    print("Constantine III has taken his army to Gaul and left Britannia\n\
          defenceless.")
    print("You are a lone Roman Centurion, the last at your fort.\n")
    print("Your Pilus Prior (commander of your cohort) has left a mission\n\
    for you.")
    print("If within 6 months, the army does not return seek out... .\n")
    print("Flavius Sanctus in Aquae Sulis.\n")

    two_choice_option("Do you go West to Aquae Sulis or South \n\
    to Durnovana? (west/south): \n",
                      "west", "south", road_west, road_south)


# Western route. **************************************************************
def road_west():

    print("\nYou take the road West, off the main Fosse Way, towards \n\
    Aquae Sulis.")
    print("As you a approach a bend in the road you spot a lone\n\
    Celtic bandit")

    two_choice_option("Do you attack the bandit or try\n\
    to hide? (attack/hide): \n",
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


# Town of Aquae Sulis. *****************************************************
def as_guards():
    print("\nThe centurion greets you in return and asks what brings you\n\
         this way... \n")
    print("alone in these dangerous times. You explain you are on a\n\
         mission left...")
    print("by your Pilus Prior.\n")

    three_choice_option("Ask what happened to the town?(town)\n\
         the townspeople? (people)\n\
         or Flavius Sanctus? (flavius)\n",
                        "town",
                        "people", "flavius", as_town, as_people, as_flavius)


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
                        "avenue",
                        "people", "town", as_avenue, as_people, as_town)


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
                        "temple",
                        "theatre", "bath", as_temple, as_theatre, as_bath)


def as_temple():
    print("You walk towards the modest square, wooden temple, dedicated\n\
    to the godess Sulis Minerva.\n")
    print("As you enter through the front, you notice members of the\n\
    godess's cult making offerings...\n")
    print("to her statue, enshrined on an alter at the rounded back\n\
    of the temple.\n")

    two_choice_option("Explore the theatre? (theatre)\n\
        or continue to the baths, forum and basilica? (bath)\n",
                      "theatre", "bath", as_theatre, as_bath)


def as_theatre():
    print("As you approach the amphitheatre you notice all of the wooden\n\
    benches have been...\n")
    print("either broken or burned, leaving behind the stone steps\n\
    underneath.")
    print("Some of the masonry has started to crumble as well. It is a\n\
    shadow of its former self.")

    two_choice_option("Explore the temple? (temple)\n\
        or continue to the baths, forum and basilica? (bath)\n",
                      "temple", "bath", as_temple, as_bath)


def as_bath():
    print("You walk further along the East-West avenue, towards the baths,\n\
    forum and basilica\n")

    three_choice_option("Explore the baths? (thermae),\n\
        the forum? (forum)\n\
        or the basilica? (basilica)\n",
                        "thermae",
                        "forum", "basilica", as_thermae, as_forum, as_basilica)


def as_thermae():
    print("The baths are a large complex of stone buildings, split up into\n\
    naturally....\n")
    print("& furnace heated baths of differing temperatures as well as sweat\n\
    rooms.\n")
    print("It seems to be well maintained, despite the state of the rest of\n\
    the town...\n")
    print("and you can hear that the furnaces are still being operated.\n")
    print("If you had more time, you would like to enjoy their use.\n")

    two_choice_option("Explore the forum? (forum)\n\
        or the basilica? (basilica)\n",
                      "forum", "basilica", as_forum, as_basilica)


def as_forum():
    print("You approach the forum, a large open rectangular space surrounded\n\
    by columns.\n")
    print("It is normally the site of all the towns major social,\n\
    political and...\n")
    print("religious gatherings and festivals, but there are signs\n\
    it hasn't...\n")
    print("been used in a some time. Debris and animal excrement\n\
    litter the cobbles.\n")

    two_choice_option("Explore the baths? (thermae) or the basilica?\n\
    (basilica)\n",
                      "thermae", "basilica", as_thermae, as_basilica)


def as_basilica():
    print("The basilica is a large rectangular stone building with a\n\
    vaulted...\n")
    print("roof, very similar in layout to a modern church. It serves\n\
    the purpose...\n")
    print("of court house, administrative center as well as many other\n\
    functions.\n")
    print("There are many members of a cohort standing gathered all around\n\
    the interior.\n")
    print("At the far end you spot Flavius Sanctus speaking to members\n\
    of the cohort.\n")

    cont("Type cont to continue. (cont):\n",
         "cont", the_mission)


def the_mission():
    print("As you approach, Flavius turns towards you and says...\n")
    print(f"'Ah {PLAYER_NAME}. Welcome. Right on time, just as\n\
    Gnaeus Calvinus...\n")
    print("said you would be.' This takes you aback somewhat.\n")
    print("As far as you were aware, this was just a contingency plan.\n")
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
    print("First though, make sure you get some rest.\n")
    print("We will speak more in the morning.")
    cont("Type cont to continue. (cont):\n",
         "cont", the_mission_3)


def the_mission_3():
    print("You wake with the sunrise. After washing and getting some...")
    print("food, you are taken by one of the centurions to meet Flavius.")
    print("'I hope your rest was good' says Flavius.")
    print("'You have a possibly long and dangerous journey ahead'")
    print("'You must set out immediatly, but I can offer some help'")
    print("'A century (up to 100 men) of the towns cohort can join you.'")

    two_choice_option("Take the offer of the century? (cent)\n\
        or depart alone? (solo)\n",
                      "cent", "solo", south_cent, south_solo)


def south_cent():
    global has_century
    has_century = True
    print("You take the generous offer and set out with the centurions...")
    print("towards Durnovaria.")
    print("Along the way you come across a large group of Saxon bandits,")
    print("but they are no match for you and the 100 warriors at...")
    print("your side.")

    cont("Type cont to continue. (cont):\n",
         "cont", durnovaria_east_gate)


def south_solo():
    print("You head off on your own, figuring you may be able to use...\n")
    print("stealth to your advantage.")

    cont("Type cont to continue. (cont):\n",
         "cont", road_south)


# Southern route.
def road_south():
    global has_century
    has_century = False
    print("You take the road South towards Durnovana. \n")
    print("In the distance you see a large group of Saxon bandits\n\
        approaching. \n")
    print("They haven't seen you yet. \n")

    two_choice_option("Do you attack the bandits or try to\n\
        hide? (attack/hide): \n",
                      "attack", "hide", attack_s_bandits, hide_s_bandits)


def attack_s_bandits():

    print("You attempt to surprise the bandits with an attack, but they\n\
        are too many & you are... \n")
    print("overwhelmed. \n")
    game_over("You are gravely wounded and die below the roadside,\n\
        mission incomplete.\n",
              start_game)


def hide_s_bandits():

    print("You successfully hide in a ditch by the roadside and the\n\
        bandits pass you by.\n")

    cont("Type cont to continue. (cont):\n",
         "cont", durnovaria_east_gate)


# Durnovaria
def durnovaria_east_gate():
    print("From a distance you can see smoke rising over the town.\n")
    print("As you approach the smaller East gate over the river...\n")
    print("you see the watchpost above it ablaze and no guards...\n")
    print("in sight. You continue on towards the East-West avenue.\n")

    cont("Type cont to continue. (cont):\n",
         "cont", dv_avenue)


def dv_avenue():
    if has_century:
        cont("You head along the avenue towards the forum, but\n\
        a group of Saxons equal in size to your own stands in your way.\n\
        you have no choice but to fight them. It's a grueling battle...\n\
        and 30 centurions are lost, but you somehow survive and defeat...\n\
        every last Saxon. Type cont to continue. (cont):\n",
             "cont", dv_forum)
    else:
        game_over("You head along the avenue towards the forum, but\n\
        a huge group of Saxons stands in your way. They've noticed you,\n\
        so you have no choice but to fight them. You are slayed on the\n\
        spot by the Saxon marauders", start_game)


def dv_forum():
    print("The forum is a mess of dead bodies and fallen columns.")
    print("To the South are the baths and to the North is the Basilica.")

    two_choice_option("Do you head towards the baths (baths), or the\n\
        basilica? (basilica):\n",
                      "baths", "basilica", dv_thermae, dv_basilica)


def dv_thermae():
    print("The baths are a burnt out husk. One half of the main...")
    print("building has collapsed into the baths themselves.")
    print("There is nothing more to see here.")

    cont("Type cont to continue. (cont):\n",
         "cont", dv_basilica)


def dv_basilica():
    print("You finally reach the basilica. A group of centurions...")
    print("are guarding the front and look very relieved to see...")
    print("your group.")
    print("Their leader welcomes you in and says Lucius Septimius...")
    print("is waiting for you inside.")

    cont("Type cont to continue. (cont):\n",
         "cont", journeys_end)


def journeys_end():
    print("Lucius Septimius greets you warmly.")
    print("You hand him the scroll and as he reads ithe nods with...")
    print("a grim look on his face.")
    print("'I am sorry to say this, but there is very little hope...")
    print("left for Britannia.'")
    print("He disappears for a moment and returns with another scroll.")
    print(f"'I am sorry my friend {PLAYER_NAME}, but your...'")
    print("'journey has only just begun.'")
    print("'You must bring this to Rome by way of Gaul.'")
    print("'It is our last and only chance.'")
    game_win("To be continued....", 
             start_game)


start_game()
