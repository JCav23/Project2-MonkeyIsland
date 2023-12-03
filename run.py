# expect a terminal of 80 characters wide and 24 rows high
import colorama
from colorama import Fore
from art import *
import sys
import time
from random import randint
colorama.init(autoreset=True)

inventory = []
galley_visited = []
chef_visited = []
required = ['Jolly Roger Flag',
            'Cinnamon Stick',
            'Gunpowder',
            'Fine Wine',
            'Ink']


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
            typewriter('You wrack your brain to remember ')
            typewriter('the ingredients required to brew the magic potion\n')
            typewriter('You remember that you need to find...\n')
            print(f"{Fore.GREEN}{required}")
            choice = input(f"{decision}")
        else:
            print(f"Invalid: must be one of the following inputs: {accepted}")
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
    typewriter('The villainous ghost pirate LeChuck')
    typewriter('has kidnapped Governor Elaine Marley\n')
    typewriter('You have procured your own pirate ship and assembled a crew\n')
    typewriter('You must now pursue LeChuck')
    typewriter('back to his hideout on Monkey Island\n')
    user_state = input("Are you ready to begin the adventure: Y/N \n").lower()
    valid = validate_input(user_state, ['y', 'n'],
                           "Are you ready to begin the adventure: Y/N \n")
    return valid


def game_over():
    """
    Displays Game Over screen and gives choice to restart
    """
    print(f"{Fore.RED}{gameover}")
    typewriter('Well I guess Elaine can fend for herself and LeChuck wins\n')
    typewriter('Some pirate you turned out to be...\n')
    user_state = input("Would you like to try again: Y/N \n").lower()
    valid = validate_input(user_state, ['y', 'n'],
                           "Would you like to try again: Y/N \n")
    return valid


def goodbye():
    """
    Goodbye screen if the player chooses not to try again following Game Over
    """
    print(f"{Fore.CYAN}{exit_message}")
    typewriter('Thank you for playing, I hope you enjoyed the adventure\n')
    typewriter('Come back and try again soon\n')
    valid = 'goodbye'
    return valid


def start_adventure():
    """
    First game choice; sets scene for player and explains how to proceed
    """
    print(f"{Fore.YELLOW}{pirate_ship}")
    typewriter('You have set sail with your crew and are')
    typewriter('stood aboard the deck of your ship The Sea Monkey\n')
    typewriter('Your crew have decided this is more of a ')
    typewriter('leisurely cruise rather than a rescue mission\n')
    typewriter('You will need to brew the magic potion ')
    typewriter('enabling travel to Monkey Island yourself\n')
    typewriter('Explore the ship and find:\n')
    print(f"{Fore.GREEN}{required}")
    typewriter('Items will be added to your inventory')
    typewriter(' automatically as you find them\n')
    typewriter('Use the "INVENTORY" or "REQUIRED" commands ')
    typewriter('at any input to see what you have found/need to find\n')
    typewriter('You are on the deck, before you is the ')
    typewriter('ladder to the crow\'s nest, a door to the captain\'s cabin\n')
    typewriter('Or stairs leading below deck, the choice is yours...\n')
    user_state = input("""
    Where will you go: LADDER/DOOR/STAIRS\n
    """).lower()
    valid = validate_input(user_state,
                           ['ladder', 'door', 'stairs'],
                           "Where will you go: LADDER/DOOR/STAIRS\n")
    return valid


def ship_deck():
    """
    Exploration event; player is on the main deck of ship
    """
    print(f"{Fore.YELLOW}{pirate_ship}")
    typewriter('You are on the deck, before you is ')
    typewriter('the ladder to the crow\'s nest, ')
    typewriter('a door to the captain\'s cabin\n')
    typewriter('Or stairs leading below deck, the choice is yours...\n')
    user_state = input("""
    Where would you like to go: LADDER/DOOR/STAIRS\n
    """).lower()
    valid = validate_input(user_state,
                           ['ladder', 'door', 'stairs'],
                           "Where would you like to go: LADDER/DOOR/STAIRS\n")
    return valid


def crows_nest():
    """
    Game event to give the player the Jolly Roger Flag
    """
    print(f"{Fore.YELLOW}{pirate_flag}")
    typewriter('You climb the ladder up to the crows nest\n')
    typewriter('This is a lot higher than you thought it would be, ')
    typewriter('maybe don\'t look down...\n')
    typewriter('After nearly losing your footing twice')
    typewriter('and what feels like an eternity of climbing...\n')
    typewriter('You finally reach the top and see the ')
    typewriter('ship\'s Jolly Roger Flag flapping in the breeze\n')
    typewriter('You take down the flag and fold it up ')
    typewriter('and take it with you as you climb back down\n')
    item = required[0]
    inventory.append(item)
    valid = ship_deck()
    return valid


def cabin_door():
    """
    Game event; if player does not have key the door will be locked
    """
    print(f"{Fore.RED}{key}")
    typewriter('You approach the door as grand and as ')
    typewriter('wooden as a door to the captain\'s quarters ought to be\n')
    typewriter('You try the handle but the door ')
    typewriter('does not budge, it must be locked\n')
    typewriter('You will have to find the key\n')
    valid = ship_deck()
    return valid


def captains_cabin():
    """
    Exploration event; triggers on first visit, player is in cabin
    """
    print(f"{Fore.YELLOW}{bed}")
    typewriter('You stroll through the door ')
    typewriter('and into a cabin fit for a king...\n')
    typewriter('Well fit for a captain...\n')
    typewriter('Well fit enough for you anyway...\n')
    typewriter('You see a rusty old rapier mounted on the wall ')
    typewriter('above the bed, a dusty old desk next to the window\n')
    typewriter('And a rickety wardrobe with one door ')
    typewriter('barely still attached, hanging by it\'s hinges\n')
    user_state = input("""
    Where will you go: SWORD/DESK/WARDROBE/LEAVE CABIN\n
    """).lower()
    valid = validate_input(user_state,
                           ['sword', 'desk', 'wardrobe', 'leave cabin'],
                           """
                           Where will you go: SWORD/DESK/WARDROBE/LEAVE CABIN\n
                           """)
    return valid


def no_sword_cabin():
    """
    Exploration event; triggers if player is in cabin but already has sword
    """
    print(f"{Fore.YELLOW}{bed}")
    typewriter('You look around the captain\'s cabin, ')
    typewriter('you see a dusty old desk next to the window\n')
    typewriter('And a rickety wardrobe with one door ')
    typewriter('barely still attached, hanging by it\'s hinges\n')
    user_state = input("""
    Where will you go: DESK/WARDROBE/LEAVE CABIN\n
    """).lower()
    valid = validate_input(user_state,
                           ['desk', 'wardrobe', 'leave cabin'],
                           """
                           Where will you go: DESK/WARDROBE/LEAVE CABIN\n
                           """)
    return valid


def cabin():
    """
    Exploration event; triggers if the player is in the cabin without the sword
    """
    print(f"{Fore.YELLOW}{bed}")
    typewriter('You look around the captain\'s cabin, ')
    typewriter('You see an old rapier mounted on the wall above the bed\n')
    typewriter('You also see a dusty old desk next to the window\n')
    typewriter('And a rickety wardrobe with one door')
    typewriter(' barely still attached, hanging by it\'s hinges\n')
    user_state = input("""
    Where will you go: SWORD/DESK/WARDROBE/LEAVE CABIN\n
    """).lower()
    valid = validate_input(user_state,
                           ['sword', 'desk', 'wardrobe', 'leave cabin'],
                           """
                           Where will you go: SWORD/DESK/WARDROBE/LEAVE CABIN\n
                           """)
    return valid


def take_sword():
    """
    Game event; gives the player the Rusty Rapier item
    """
    print(f"{Fore.YELLOW}{sword}")
    typewriter('Technically, you are the captain of ')
    typewriter('this ship now so that sword should belong to you\n')
    typewriter('So this can\'t be considered stealing right?\n')
    typewriter('Probably best to not think too hard about it\n')
    typewriter('You take the sword down off the wall and take it with you\n')
    item = 'Rusty Rapier'
    inventory.append(item)
    valid = no_sword_cabin()
    return valid


def check_desk():
    """
    Game Event; gives the player the required ink item
    """
    print(f"{Fore.YELLOW}{inkwell}")
    typewriter('You walk over to the writing desk, ')
    typewriter('and examine the dusty papers scattered across it\n')
    typewriter('Your eyes stop as you catch ')
    typewriter('sight of an old inkwell and quill\n')
    typewriter('You remove the quill and leave ')
    typewriter('it on the desk, and put the inkwell in your pocket\n')
    item = required[4]
    inventory.append(item)
    if 'Rusty Rapier' in inventory:
        valid = no_sword_cabin()
    else:
        valid = cabin()
    return valid


def check_wardrobe():
    """
    Game Event; gives the player the required Fine Wine item
    """
    print(f"{Fore.YELLOW}{wine}")
    typewriter('You approach the wardrobe and ')
    typewriter('carefully try to open the door without damaging it\n')
    typewriter('Inside the wardrobe you see a moth-eaten ')
    typewriter('coat that was probably very fine in a previous life\n')
    typewriter('Checking the shelves you notice ')
    typewriter('tucked away on the bottom a bottle of wine\n')
    typewriter('You attempt to read the label but it ')
    typewriter('is in French and you were never good with languages\n')
    typewriter('Never the less this is exactly ')
    typewriter('what you need and take the bottle with you\n')
    item = required[3]
    inventory.append(item)
    if 'Rusty Rapier' in inventory:
        valid = no_sword_cabin()
    else:
        valid = cabin()
    return valid


def descend_below_deck():
    """
    Exploration Event; the player moves below deck and given options
    """
    print(f"{Fore.YELLOW}{cannon}")
    typewriter('You descend the stairs taking you ')
    typewriter('below deck, a battery of cannons line both walls\n')
    typewriter('You cast your eyes around, you see a door to the galley,\n')
    if 'Gunpowder' in inventory:
        typewriter('Some barrels marked "GUNPOWDER" with the cargo net')
        typewriter(' that secured them laying in tatters on floor,\n')
    else:
        typewriter('Some barrels marked "GUNPOWDER" ')
        typewriter('lashed to the port bow with cargo net,\n')
    typewriter('And the stairs leading back up above deck\n')
    user_state = input("""
    Where will you go: GALLEY/BARRELS/UPSTAIRS/CANNON\n
    """).lower()
    valid = validate_input(user_state,
                           ['galley', 'barrels', 'upstairs', 'cannon'],
                           """
                           Where will you go: GALLEY/BARRELS/UPSTAIRS/CANNON\n
                           """)
    return valid


def below_deck():
    """
    Exploration Event; the player is below deck coming from the galley
    """
    print(f"{Fore.YELLOW}{cannon}")
    typewriter('You are stood below deck, you see the door ')
    typewriter('to the galley, the cannon\'s lining both walls,\n')
    if 'Gunpowder' in inventory:
        typewriter('Some barrels marked "GUNPOWDER" with the cargo ')
        typewriter('net that secured them laying in tatters on floor,\n')
    else:
        typewriter('Some barrels marked "GUNPOWDER" lashed ')
        typewriter('to the port bow with cargo net,\n')
    typewriter('And the stairs leading back up above deck\n')
    user_state = input("""
    Where will you go: GALLEY/BARRELS/UPSTAIRS/CANNON\n
    """).lower()
    valid = validate_input(user_state,
                           ['galley', 'barrels', 'upstairs', 'cannon'],
                           """
                           Where will you go: GALLEY/BARRELS/UPSTAIRS/CANNON\n
                           """)
    return valid


def cannon_event():
    """
    Game Event; triggers game over for player if they make this choice
    """
    print(f"{Fore.RED}{explosion}")
    typewriter('You suddenly have a great idea, it may ')
    typewriter('be the greatest idea you have ever had\n')
    typewriter('You are not quite sure what you hope to ')
    typewriter('accomplish but this good of an idea should not be ignored\n')
    typewriter('You prime the cannon, light it and climb inside the barrel\n')
    typewriter('With a deafening "BOOM" the cannon')
    typewriter(' fires you through the side of the ship\n')
    typewriter('As you sail through the air suddenly ')
    typewriter('you think this may not have been the best idea\n')
    typewriter('With a splash you land in open water, ')
    typewriter('with no ship in sight and sharks beginning to circle\n')
    typewriter('That definitely wasn\'t a good idea you ')
    typewriter('think to yourself as a shark pulls you beneath the water\n')
    valid = game_over()
    return valid


def powder_barrels():
    """
    Game Event; if player has acquired sword they will obtain the Gunpowder
    """
    if 'Rusty Rapier' in inventory:
        print(f"{Fore.YELLOW}{barrel}")
        typewriter('You draw the Rusty Rapier and ')
        typewriter('used it to cut away the cargo net\n')
        typewriter('You can now get into the barrel\'s\n')
        typewriter('You remove the lid from one ')
        typewriter('of the barrels and peer inside,\n')
        typewriter('Sure enough it is filled to the brim with powder\n')
        typewriter('You take a handful and put it in your pocket\n')
        item = required[2]
        inventory.append(item)
        valid = below_deck()
    else:
        print(f"{Fore.RED}{barrel}")
        typewriter('You tug at the cargo net securing the barrels in place\n')
        typewriter('The net however does not budge, ')
        typewriter('and you are unable to get into the barrels\n')
        typewriter('Perhaps you can find something to cut the net\n')
        valid = below_deck()
    return valid


def first_galley_visit():
    """
    Exploration Event; Player enters the ship galley for the first time
    """
    print(f"{Fore.YELLOW}{cauldron}")
    galley_visited.append('YES')
    typewriter('As you wander into the ship\'s galley you ')
    typewriter('notice a curious, unpleasant smell\n')
    typewriter('You sincerely hope that it\'s not ')
    typewriter('the chef\'s cooking and are very glad that pirates are\'t\n')
    typewriter('Subjected to visits from the Health inspector ')
    typewriter('as you would most definitely be slapped with a fine\n')
    typewriter('You see a large pot bubbling on the stove, ')
    typewriter('this is where you will need to brew the potion\n')
    typewriter('Looking around the room you also ')
    typewriter('see the Chef prepping for tonight\'s supper,\n')
    typewriter('and a cupboard marked "PANTRY"\n')
    user_state = input("""
    Where will you go: PANTRY/CHEF/CAULDRON/LEAVE GALLEY\n
    """).lower()
    valid = validate_input(user_state,
                           ['pantry', 'chef', 'cauldron', 'leave galley'],
                           """
                           Where will you go: PANTRY/CHEF/CAULDRON/LEAVE GALLEY\n
                           """)
    return valid


def galley():
    """
    Exploration Event; Player enters the galley
    """
    print(f"{Fore.YELLOW}{cauldron}")
    typewriter('You see a large pot bubbling on the stove, ')
    typewriter('this is where you will need to brew the potion\n')
    typewriter('Looking around the room you also ')
    typewriter('see the Chef prepping for tonight\'s supper,\n')
    typewriter('and a cupboard marked "PANTRY"\n')
    user_state = input("""
    Where will you go: PANTRY/CHEF/CAULDRON/LEAVE GALLEY\n
    """).lower()
    valid = validate_input(user_state,
                           ['pantry', 'chef', 'cauldron', 'leave galley'],
                           """
                           Where will you go: PANTRY/CHEF/CAULDRON/LEAVE GALLEY\n
                           """)
    return valid


def check_pantry():
    """
    Game Event; Gives the player the Cinnamon Stick item
    """
    print(f"{Fore.YELLOW}{rat}")
    typewriter('As you open the doors to the pantry, ')
    typewriter('a rat scurries out of the cupboard and down your arm\n')
    typewriter('It dashes out of the door as you let out a cowardly shriek\n')
    typewriter('You hear the Chef chuckle to himself behind you\n')
    typewriter('You look through the dusty ')
    typewriter('shelves of the poorly stocked pantry\n')
    typewriter('You see a few bottles of grog, ')
    typewriter('some tins of spices and a single cinnamon stick\n')
    typewriter('You grab the cinnamon stick and close the cupboard doors\n')
    item = required[1]
    inventory.append(item)
    valid = galley()
    return valid


def hangman():
    """
    Game Event; Triggers a game of hangman for the player
    """
    alphabet = ["a", "b", "c", "d", "e", "f",
                "g", "h", "i", "j", "k", "l", "m",
                "n", "o", "p", "q", "r", "s",
                "t", "u", "v", "w", "x", "y", "z"]
    word_list = ['pirate', 'cannon', 'monkey', 'captain', 'swashbuckler']
    random = randint(0, 4)
    word = word_list[random]
    length = len(word)
    game_board = []
    lives = 5
    game_active = True
    valid = 0
    for char in range(length):
        game_board += '_'
    while game_active:
        choice = input('Guess a letter: \n').lower()
        if choice not in alphabet:
            print(f'{Fore.RED}Invalid: Choice must be letter')
        elif choice in game_board:
            print(f'{Fore.RED}You\'ve already chosen {choice}, pick again')
        elif choice not in word:
            print(f'{Fore.RED}Incorrect, lose a life')
            lives -= 1
            print(f'{Fore.RED}{lives}')
            if lives == 0:
                print(f'{Fore.RED}GAME OVER')
                valid = 'lose'
                game_active = False
        for index in range(length):
            letter = word[index]
            if letter == choice:
                game_board[index] = letter
        print(f"{Fore.BLUE}{' '.join(game_board)}")
        if "_" not in game_board:
            print(f'{Fore.GREEN}YOU WIN')
            game_active = False
            valid = 'win'
    return valid


def chef():
    """
    Game Event; introduces the player to Chef character, play game to win item
    """
    print(f"{Fore.YELLOW}{cook}")
    chef_visited.append('YES')
    typewriter('The chef regards you with disdain "I\'ve ')
    typewriter('found the key to the captain\'s cabin"\n')
    typewriter('"You should be more careful not to lose things, ')
    typewriter('if you want it back you\'ll have to win it"\n')
    typewriter('He pull\'s out an old chalkboard and ')
    typewriter('prepares a game of hangman for you\n')
    typewriter('Looks like you\'ll have to play his game ')
    typewriter('if you want to get into the captain\'s cabin\n')
    valid = hangman()
    if valid == 'win':
        typewriter('The chef looks dejected... "Best two out of three?"\n')
        typewriter('You begin shouting a stream of profanities at the chef\n')
        typewriter('It is a long list of words that should ')
        typewriter('never be uttered in civil society\n')
        typewriter('The chef finally relents, and hands over the key ')
        typewriter('"Okay, no need to shout, I was just having fun\n')
        item = 'Cabin Key'
        inventory.append(item)
        valid = galley()
    else:
        typewriter('The chef roars with laughter at your failure\n')
        typewriter('"You\'ll have to do better than that, ')
        typewriter('come back if you ever want to try again"\n')
        valid = galley()
    return valid


def replay_chef():
    print(f"{Fore.YELLOW}{cook}")
    typewriter('"Ready to try again?" he says as ')
    typewriter('he pulls out the chalkboard again\n')
    valid = hangman()
    if valid == 'win':
        typewriter('The chef looks dejected... "Best two out of three?"\n')
        typewriter('You begin shouting a stream of profanities at the chef\n')
        typewriter('It is a long list of words that ')
        typewriter('should never be uttered in civil society\n')
        typewriter('The chef finally relents, and hands over ')
        typewriter('the key "Okay, no need to shout, I was just having fun\n')
        item = 'Cabin Key'
        inventory.append(item)
        valid = galley()
    else:
        typewriter('The chef roars with laughter at your failure\n')
        typewriter('"You\'ll have to do better than that, ')
        typewriter('come back if you ever want to try again"\n')
        valid = galley()
    return valid


def endgame():
    """
    Final screen of the game display Win message
    """
    print(f"{Fore.GREEN}{winner}")
    typewriter('You have done it, you have reached Monkey Island\n')
    typewriter('You are able to defeat the Ghastly ')
    typewriter('Ghost Pirate LeChuck and rescue Elaine\n')
    typewriter('You really are the greatest pirate to have ever lived\n')
    valid = goodbye()
    return valid


def brew_potion():
    """
    Game Event; if players interact with cauldron
    with all required items, endgame will trigger
    """
    print(f"{Fore.GREEN}{cauldron}")
    typewriter('After a painstaking search finding ')
    typewriter('all of the items you needed\n')
    typewriter('You throw each of the items into the ')
    typewriter('large pot bubbling on the stove\n')
    typewriter('After the last item lands with a ')
    typewriter('splash in the pot, smoke begins to billow out\n')
    print(f"{Fore.CYAN}{explosion}")
    typewriter('With a almighty BANG there is a ')
    typewriter('magical explosion and you are knocked unconscious\n')
    typewriter('When you awaken you realise ')
    typewriter('you have arrived at Monkey Island\n')
    typewriter('It\'s time to face LeChuck\n')
    valid = endgame()
    return valid


def validate_items():
    correct_items = 0
    for item in required:
        if item in inventory:
            correct_items += 1
    if correct_items == 5:
        return True
    else:
        typewriter(f'You only have {correct_items} of the required items')
        return False


def main():
    """
    Main Game loop; while loop and control flow monitors
    game progress evaluated by player input and inventory
    """
    inventory.clear()
    galley_visited.clear()
    chef_visited.clear()
    valid = start_game()
    if valid == 'y':
        valid = start_adventure()
        exploration = True
        while exploration:

            if valid == 'ladder':
                if 'Jolly Roger Flag' in inventory:
                    typewriter('You are certain there was nothing ')
                    typewriter('more of use up there and besides...\n')
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

            elif valid == 'desk':
                if 'Ink' in inventory:
                    typewriter('You didn\'t see anything ')
                    typewriter('else useful on the desk\n')
                    if 'Rusty Rapier' in inventory:
                        valid = no_sword_cabin()
                    else:
                        valid = cabin()
                else:
                    valid = check_desk()

            elif valid == 'wardrobe':
                if 'Fine Wine' in inventory:
                    typewriter('While that coat was very fancy in it\'s day ')
                    typewriter('it it too damaged to be worth wearing\n')
                    typewriter('Aside from that there was ')
                    typewriter('nothing else of note in the wardrobe\n')
                    if 'Rusty Rapier' in inventory:
                        valid = no_sword_cabin()
                    else:
                        valid = cabin()
                else:
                    valid = check_wardrobe()

            elif valid == 'sword':
                valid = take_sword()

            elif valid == 'leave cabin':
                valid = ship_deck()

            elif valid == 'galley':
                if galley_visited:
                    valid = galley()
                else:
                    valid = first_galley_visit()

            elif valid == 'leave galley':
                valid = below_deck()

            elif valid == 'pantry':
                if 'Cinnamon Stick' in inventory:
                    typewriter('You didn\'t see anything ')
                    typewriter('else useful in there\n')
                    typewriter('And you do not want to ')
                    typewriter('tangle with another rat\n')
                    valid = galley()
                else:
                    valid = check_pantry()

            elif valid == 'chef':
                if 'Cabin Key' in inventory:
                    typewriter('You already have the key from the Chef ')
                    typewriter('and you are in no mood for another game\n')
                    valid = galley()
                else:
                    if chef_visited:
                        valid = replay_chef()
                    else:
                        valid = chef()

            elif valid == 'barrels':
                if 'Gunpowder' in inventory:
                    typewriter('You already have a pocket full of ')
                    typewriter('gunpowder which is pretty dangerous as is\n')
                    typewriter('You won\'t need anymore\n')
                    valid = below_deck()
                else:
                    valid = powder_barrels()

            elif valid == 'cannon':
                exploration = False
                valid = cannon_event()
                if valid == 'y':
                    main()
                elif valid == 'n':
                    goodbye()

            elif valid == 'cauldron':
                valid = validate_items()
                if valid:
                    exploration = False
                    valid = brew_potion()
                else:
                    valid = galley()

    elif valid == 'n':
        valid = game_over()
        if valid == 'y':
            main()
        elif valid == 'n':
            goodbye()
    else:
        print("Unforeseen Error: Please Restart")


main()
