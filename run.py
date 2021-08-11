def intro_msg():


    """
    Function to print welcome graphics.
    """

    print()
    typing("##################################\n", 0.01)
    typing("#                                #\n", 0.01)
    typing("#   The Fall of Roman Britain    #\n", 0.01)
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
        if PLAYER_NAME = "":
            print("Please enter a character name to continue...\n")
            continue
        else:
            break
    typing(f"Salve {PLAYER_NAME}. Alae iacta est! (Greetings {PLAYER_NAME}. The die is cast!\n\n, 0,03")
    option_one()
