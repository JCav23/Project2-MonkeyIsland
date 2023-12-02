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
                print(f"{Fore.CYAN}{inventory}")
                choice = input(f"{decision}")
            else:
                typewriter("Your pockets are empty...\n")
                choice = input(f"{decision}")
        elif choice == 'required':
            typewriter('You wrack your brain to remember the ingredients required to brew the magic potion\n')
            typewriter('You remember that you need to find...')
            print(f"{Fore.GREEN}{required}")
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
    typewriter('Use the "INVENTORY" or "REQUIRED" commands at any input to see what you have found/still need to find\n')
    typewriter('You are on the deck, before you is the ladder to the crow\'s nest, a door to the captain\'s cabin\n')
    typewriter('Or stairs leading below deck, the choice is yours...\n')
    user_state = input("Where would you like to go? : LADDER/DOOR/STAIRS\n").lower()
    valid = validate_input(user_state, ['ladder', 'door', 'stairs'],
                           "Where would you like to go? : LADDER/DOOR/STAIRS\n")
    return valid


def ship_deck():
    """
    Exploration event; the player is on the main deck of the ship and can choose where to explore
    """
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


def cabin_door():
    """
    Game event; if player does not have key the door will be locked forcing more exploration
    """
    print(f"{Fore.RED}{key}")
    typewriter('You approach the door as grand and as wooden as a door to the captain\'s quarters ought to be\n')
    typewriter('You try the handle but the door does not budge, it must be locked\n')
    typewriter('You will have to find the key\n')
    valid = ship_deck()
    return valid


def captains_cabin():
    """
    Exploration event; player has the choice to explore the room looking for items
    """
    print(f"{Fore.YELLOW}{sword}")
    typewriter('You stroll through the door and into a cabin fit for a king...\n')
    typewriter('Well fit for a captain...\n')
    typewriter('Well fit enough for you anyway...\n')
    typewriter('You see a rusty old rapier mounted on the wall above the bed, a dusty old desk next to the window\n')
    typewriter('And a rickety wardrobe with one door barely still attached, hanging by it\'s hinges')
    user_state = input('What would you like to do? : SWORD/DESK/WARDROBE/LEAVE CABIN\n').lower()
    valid = validate_input(user_state, ['sword', 'desk', 'wardrobe', 'leave cabin'],
                           'What would you like to do? : SWORD/DESK/WARDROBE/LEAVE CABIN\n')
    return valid


def cabin():
    """
    Exploration event; triggers if the player is in the cabin but already has the sword in inventory
    """
    typewriter('You look around the captain\'s cabin, you see a dusty old desk next to the window\n')
    typewriter('And a rickety wardrobe with one door barely still attached, hanging by it\'s hinges\n')
    user_state = input('What would you like to do? : DESK/WARDROBE/LEAVE CABIN\n').lower()
    valid = validate_input(user_state, ['desk', 'wardrobe', 'leave cabin'],
                           'What would you like to do? : SWORD/DESK/WARDROBE/LEAVE CABIN\n')
    return valid


def take_sword():
    """
    Game event; gives the player the Rusty Rapier item
    """
    typewriter('Technically, you are the captain of this ship now so that sword should belong to you\n')
    typewriter('So this can\'t be considered stealing right?\n')
    typewriter('Probably best to not think too hard about it\n')
    typewriter('You take the sword down off the wall and take it with you\n')
    item = 'Rusty Rapier'
    inventory.append(item)
    valid = cabin()
    return valid


def descend_below_deck():
    """
    Exploration Event; the player moves below deck and given options
    """
    print(f"{Fore.YELLOW}{cannon}")
    typewriter('You descend the stairs taking you below deck, a battery of cannons line both walls\n')
    typewriter('You cast your eyes around, you notice a door to the galley,\n')
    if 'Gunpowder' in inventory:
        typewriter('Some barrels marked "GUNPOWDER" with the cargo net that secured them laying in tatters on floor,\n')
    else:
        typewriter('Some barrels marked "GUNPOWDER" lashed to the port bow with cargo net,\n')
    typewriter('And the stairs leading back up above deck\n')
    user_state = input('What would you like to do? : GALLEY/BARRELS/STAIRS/CANNON\n').lower()
    valid = validate_input(user_state, ['galley', 'barrels', 'upstairs', 'cannon'],
                           'What would you like to do? : GALLEY/BARRELS/UPSTAIRS/CANNON\n')
    return valid


def below_deck():
    """
    Exploration Event; the player is below deck coming from the galley
    """
    print(f"{Fore.YELLOW}{cannon}")
    typewriter('You are stood below deck, you see the door to the galley, the cannon\'s lining both walls,\n')
    if 'Gunpowder' in inventory:
        typewriter('Some barrels marked "GUNPOWDER" with the cargo net that secured them laying in tatters on floor,\n')
    else:
        typewriter('Some barrels marked "GUNPOWDER" lashed to the port bow with cargo net,\n')
    typewriter('And the stairs leading back up above deck\n')
    user_state = input('What would you like to do? : GALLEY/BARRELS/STAIRS/CANNON\n').lower()
    valid = validate_input(user_state, ['galley', 'barrels', 'upstairs', 'cannon'],
                           'What would you like to do? : GALLEY/BARRELS/UPSTAIRS/CANNON\n')
    return valid


def cannon_event():
    """
    Game Event; triggers a game over for the player if they make the wrong choice
    """
    print(f"{Fore.RED}{explosion}")
    typewriter('You suddenly have a great idea, it may be the greatest idea you have ever had\n')
    typewriter('You are not quite sure what you hope to accomplish but this good of an idea should not be ignored\n')
    typewriter('You prime the cannon, light it and climb inside the barrel\n')
    typewriter('With a deafening "BOOM" the cannon fires you through the side of the ship\n')
    typewriter('As you sail through the air suddenly you think this may not have been the best idea\n')
    typewriter('With a splash you land in open water, with no ship in sight and sharks beginning to circle\n')
    typewriter('That definitely wasn\'t a good idea you think to yourself as a shark pulls you beneath the water\n')
    valid = game_over()
    return valid


def powder_barrels():
    """
    Game Event; if player has acquired the sword they will obtain the Gunpowder
    """
    if 'Rusty Rapier' in inventory:
        print(f"{Fore.YELLOW}{barrel}")
        typewriter('You draw the Rusty Rapier and used it to cut away the cargo net\n')
        typewriter('You can now get into the barrel\'s')
        typewriter('You remove the lid and peer inside a barrel,\n')
        typewriter('Sure enough it is filled to the brim with powder\n')
        typewriter('You take a handful and put it in your pocket\n')
        item = required[2]
        inventory.append(item)
        valid = below_deck()
    else:
        print(f"{Fore.RED}{barrel}")
        typewriter('You tug at the cargo net securing the barrels in place\n')
        typewriter('The net however does not budge, and you are unable to get into the barrels')
        typewriter('Perhaps you can find something to cut the net')
        valid = below_deck()
    return valid


def first_galley_visit():
    """
    Exploration Event; Player enters the ship galley for the first time
    """
    print(f"{Fore.YELLOW}{cauldron}")
    typewriter('As you wander into the ship\'s galley you notice a curious, unpleasant smell')
    typewriter('You sincerely hope that it\'s not the chef\'s cooking and are very glad that pirates are\'t')
    typewriter('Subjected to visits from the Health inspector as you would most definitely be slapped with a fine\n')
    typewriter('You see a large pot bubbling on the stove, this is where you will need to brew the potion\n')
    typewriter('Looking around the room you also see the Chef prepping for tonight\'s supper,\n')
    typewriter('and a cupboard marked "PANTRY"\n')
    user_state = input('What would you like to do? : PANTRY/CHEF/CAULDRON/LEAVE GALLEY\n').lower()
    valid = validate_input(user_state, ['pantry', 'chef', 'cauldron', 'leave galley'],
                           'What would you like to do? : PANTRY/CHEF/CAULDRON/LEAVE GALLEY\n')
    return valid


def main():
    """
    Main Game loop; while loop and control flow monitors game progress evaluated by player input and inventory
    """
    inventory.clear()
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
                valid = descend_below_deck()
            elif valid == 'upstairs':
                valid = ship_deck()
            elif valid == 'door':
                if 'Cabin Key' in inventory:
                    valid = captains_cabin()
                else:
                    valid = cabin_door()
            elif valid == 'barrels':
                valid = powder_barrels()
            elif valid == 'cannon':
                exploration = False
                valid = cannon_event()
                if valid == 'y':
                    main()
                elif valid == 'n':
                    goodbye()
    elif valid == 'n':
        valid = game_over()
        if valid == 'y':
            main()
        elif valid == 'n':
            goodbye()
    else:
        print("Unforeseen Error: Please Restart")


main()

