# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import colorama
from colorama import Fore
from art import *
import sys
import time
colorama.init(autoreset=True)


def typewriter(string):
    for i in string:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.05)


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
    typewriter('You must now as pursue LeChuck back to his hideout on Monkey Island\n')
    user_state = input("Are you ready to begin the adventure: Y/N \n").lower()
    return user_state



start_game()


