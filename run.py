import random
import os
from words import list_of_words

def clear_screen():
    """
    Clears screen after each input
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def splash_screen():
    print(r"""
    
██   ██  █████  ███    ██  ██████  ███    ███  █████  ███    ██ 
██   ██ ██   ██ ████   ██ ██       ████  ████ ██   ██ ████   ██ 
███████ ███████ ██ ██  ██ ██   ███ ██ ████ ██ ███████ ██ ██  ██ 
██   ██ ██   ██ ██  ██ ██ ██    ██ ██  ██  ██ ██   ██ ██  ██ ██ 
██   ██ ██   ██ ██   ████  ██████  ██      ██ ██   ██ ██   ████ 
                                                                
    """)

    options = input('Press 1 to start game. Press 2 for instructions: ')

    if options.isdigit():
        choice = int(options)
        if choice == '1':
            pass
        elif options == '2':
            clear_screen()
            return instructions()
        else:
         print('Invalid input. Press 1 to start, or press 2 for instructions.')
    else:
        print('Invalid input. Please enter a number (1 or 2)')          

def instructions():
    """
    When you click '2' on the splash screen page, this displays,
    displaying instructions of the game
    """
    print('Thank you for choosing to play Hangman!\n')
    print('The objective of the game is simple!\n')
    print('It is to guess what the hidden word is before the stick figure is hung.\n')
    print('Start guessing letters when prompted')
    print('Choose your letters wisely, you have 7 lives!\n')
    print('The game ends when you either guess the correct word or you run out of lives.\n')

    back = input('Press 1 to go back to menu: ')
    if back == '1':
        clear_screen()
        return splash_screen()
    else:
        print('Invalid input. Press 1 to go back to menu.')        
    
def get_word():
    """
    Generates a random word from the list_of_words.
    """
    word = random.choice(list_of_words)
    return word               

def main():
    splash_screen()

main()         
