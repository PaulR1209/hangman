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
guessed_letter_list = []

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
                clear_screen()
                run_game()
                break    
            elif options == 2:
                clear_screen()
                instructions()
                break    
            else:
                raise ValueError ('Only 1 or 2 are allowed, try again.')
        except ValueError as e:
              clear_screen()  
              print(e)
              return main_menu()    

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

    try:
        start_game = input('Press 1 to start the game: ')
        
        if start_game == '1':
            clear_screen()
            run_game()
        else:
            raise ValueError ('Invalid input. Press 1 to go start game.\n')
    except ValueError as e:
        clear_screen()
        print(e)
        return instructions()                

def display_word(hidden_word, guessed_letter_list):
    """
    Displays hidden word with correct guesses revealed
    """
    display = ''
    for letter in hidden_word:
        if letter in guessed_letter_list:
            display += letter + ''
        else:
            display += '_ '
    print(display)        

def guessed_letter():
    """
    Asks the user to guess and input a letter
    """
    try:
        guess = input('Type a letter to make a guess: ').lower()
        if len(guess) != 1 or not guess.isalpha():
            raise ValueError('Only single letters allowed.')  
        
        if guess in guessed_letter_list:
            raise ValueError('You have already guessed this letter. Try again.')

        else:
            guessed_letter_list.append(guess)

        return guess
    except ValueError as e:
        clear_screen()
        print(e)
        return guessed_letter()            

def run_game():

    remaining_attempts = 7
    hidden_word = get_word()
    print(hangman_stages(remaining_attempts))
    guessed_letter()
    display_word(hidden_word)

main_menu()