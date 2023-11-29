# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import colorama
from colorama import Fore
from art import *
colorama.init(autoreset=True)


def start_game():
    """
    Initialise a new game
    """
    # print(f"{Fore.Green}{opening_logo}")
    print(f"{Fore.GREEN}{opening_logo}")
    data = input("Would you like to play: Y/N \n")
    return data

start_game()