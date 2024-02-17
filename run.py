import random
import os
from words import list_of_words
from ascii import splash_screen
from ascii import hangman_stages

def get_word():
    """
    Generates a random word from the list_of_words.
    """
    word = random.choice(list_of_words)
    return word

lives = 7
guessed_letters = ''

def clear_screen():
    """
    Clears screen after each input
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def main_menu():

    print(splash_screen)

    while True:
        try:
            options = int(input('Press 1 to start game. Press 2 for instructions: '))

            if options == 1:
                break    
            elif options == 2:
                clear_screen()
                instructions()
                break    
            else:
                print('Invalid input.\n')
        except ValueError:
              print('Invalid input.\n')    

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
        return main_menu()
    else:
        print('Invalid input. Press 1 to go back to menu.')        

def display_word(hidden_word):
    """
    Displays the hidden word as underscores.
    """
    print('_ '*len(hidden_word))          

def main():
    main_menu()
    

main()

remaining_attempts = 5
hidden_word = get_word()
print(hangman_stages(remaining_attempts))
display_word(hidden_word)