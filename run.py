# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import colorama
from colorama import Fore
from art import *
import sys
import time
colorama.init(autoreset=True)

inventory = []
required = ['Jolly Roger Flag', 'Cinnamon Stick', 'Gunpowder', 'Fine Wine', 'Ink']


def typewriter(string):
    for i in string:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.01)


def validate_input(actual, accepted, decision):
    """
    Validates user input using accepted criteria
    """
    cont = True
    choice = actual
    while cont:
        if choice in accepted:
            cont = False
        elif choice == 'inventory':
            if inventory:
                typewriter("You check your pockets and find...\n")
                print(f"{Fore.GREEN}{inventory}")
                choice = input(f"{decision}")
            else:
                typewriter("Your pockets are empty...\n")
                choice = input(f"{decision}")
        else:
            print(f"Invalid input: Input must be one of the following inputs: {accepted}")
            choice = input(f"{decision}")
    return choice


def start_game():
    """
    Initialise a new game
    """
    # print(f"{Fore.Green}{opening_logo}")
    print(f"{Fore.YELLOW}{opening_logo}")
    typewriter('Welcome!\n')
    typewriter('You are about to take on the role of Guybrush Threepwood\n')
    typewriter('The villainous ghost pirate LeChuck has kidnapped Governor Elaine Marley\n')
    typewriter('You have procured your own pirate ship and assembled a crew\n')
    typewriter('You must now pursue LeChuck back to his hideout on Monkey Island\n')
    user_state = input("Are you ready to begin the adventure: Y/N \n").lower()
    valid = validate_input(user_state, ['y', 'n'], "Are you ready to begin the adventure: Y/N \n")
    return valid


def game_over():
    """
    Displays Game Over screen and gives choice to restart
    """
    print(f"{Fore.RED}{gameover}")
    typewriter('Well I guess Elaine can fend for herself and LeChuck wins\n')
    typewriter('Some pirate you turned out to be...\n')
    user_state = input("Would you like to try again: Y/N \n").lower()
    valid = validate_input(user_state, ['y', 'n'], "Would you like to try again: Y/N \n")
    return valid


def goodbye():
    """
    displays Goodbye screen if the player chooses not to try again following Game Over
    """
    print(f"{Fore.CYAN}{exit_message}")
    typewriter('Thank you for playing, I hope you enjoyed the adventure\n')
    typewriter('Come back and try again soon\n')


def start_adventure():
    """
    First game choice; sets the scene for the player and gives options about how to proceed
    """
    print(f"{Fore.YELLOW}{pirate_ship}")
    typewriter('You have set sail with your crew and are stood aboard the deck of your ship The Sea Monkey\n')
    typewriter('Your crew have decided this is more of a leisurely cruise rather than a rescue mission\n')
    typewriter('You will need to brew the magic potion enabling travel to Monkey Island yourself\n')
    typewriter('Explore the ship and find:\n')
    print(f"{Fore.GREEN}{required}")
    typewriter('Items will be added to your inventory automatically as you find them\n')
    typewriter('Use the "INVENTORY" command at any input to see what you have found so far\n')
    typewriter('You are on the deck, before you is the ladder to the crow\'s nest, a door to the captain\'s cabin\n')
    typewriter('Or stairs leading below deck, the choice is yours...\n')
    user_state = input("Where would you like to go? : LADDER/DOOR/STAIRS\n").lower()
    valid = validate_input(user_state, ['ladder', 'door', 'stairs'],
                           "Where would you like to go? : LADDER/DOOR/STAIRS\n")
    return valid


def ship_deck():
    print(f"{Fore.YELLOW}{pirate_ship}")
    typewriter('You are on the deck, before you is the ladder to the crow\'s nest, a door to the captain\'s cabin\n')
    typewriter('Or stairs leading below deck, the choice is yours...\n')
    user_state = input("Where would you like to go? : LADDER/DOOR/STAIRS\n").lower()
    valid = validate_input(user_state, ['ladder', 'door', 'stairs'],
                           "Where would you like to go? : LADDER/DOOR/STAIRS\n")
    return valid


def crows_nest():
    """
    Game event to give the player the Jolly Roger Flag
    """
    print(f"{Fore.YELLOW}{pirate_flag}")
    typewriter('You climb the ladder up to the crows nest\n')
    typewriter('This is a lot higher than you thought it would be, maybe don\'t look down...\n')
    typewriter('After nearly losing your footing twice and what feels like an eternity of climbing...\n')
    typewriter('You finally reach the top and see the ship\'s Jolly Roger Flag flapping in the breeze\n')
    typewriter('You take down the flag and fold it up and take it with you as you climb back down\n')
    item = required[0]
    inventory.append(item)
    valid = ship_deck()
    return valid


def main():
    valid = start_game()
    if valid == 'y':
        valid = start_adventure()
        exploration = True
        while exploration:
            if valid == 'ladder':
                if 'Jolly Roger Flag' in inventory:
                    typewriter('You are certain there was nothing more of use up there and besides...\n')
                    typewriter('You do not fancy making that climb again\n')
                    valid = ship_deck()
                else:
                    valid = crows_nest()
            elif valid == 'stairs':
                pass
            elif valid == 'door':
                pass
    elif valid == 'n':
        valid = game_over()
        if valid == 'y':
            valid = start_game()
        elif valid == 'n':
            goodbye()
    else:
        print("Unforeseen Error: Please Restart")


main()

