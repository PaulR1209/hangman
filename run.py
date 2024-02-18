import random
import os
from colorama import Fore, init
from words import list_of_words
from ascii import splash_screen
from ascii import hangman_stages

init()
# Initialise Colorama

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
    """
    This is the start screen where you have the option
    to start the game or read the instructions
    """

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
                raise ValueError (f'{Fore.RED}Only 1 or 2 are allowed, try again.{Fore.RESET}')
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
    print('Choose your guesses wisely, you have 7 lives!\n')
    print('The game ends when you either guess the correct word or you run out of lives.\n')

    try:
        start_game = input('Press 1 to start the game: ')
        
        if start_game == '1':
            clear_screen()
            run_game()
        else:
            raise ValueError (f'{Fore.RED}Invalid input. Press 1 to go start game.\n{Fore.RESET}')
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
    return display        

def guessed_letter():
    """
    Asks the user to guess and input a letter
    """
    try:
        guess = input('Type a letter to make a guess: ').lower()
        if len(guess) != 1 or not guess.isalpha():
            raise ValueError(f'{Fore.RED}Only single letters allowed.{Fore.RESET}')  
        
        if guess in guessed_letter_list:
            raise ValueError(f'{Fore.RED}You have already guessed this letter. Try again.{Fore.RESET}')
            # need to figure out how to not have
            # error messages run down the screen
        else:
            guessed_letter_list.append(guess)

        return guess
    except ValueError as e:
        print(e)
        return guessed_letter()            

def run_game():
    """
    Runs the game logic
    """

    remaining_attempts = 7
    hidden_word = get_word()
    result_message = ''

    while remaining_attempts > 0:
        clear_screen()
        print('Lets play!\n')
        print(f'Lives: {remaining_attempts}\n')
        print(result_message)
        print(hangman_stages(remaining_attempts))
        
        display = display_word(hidden_word, guessed_letter_list)
        print(f'{display}\n')

        guess = guessed_letter()

        if guess in hidden_word:
            result_message = f'{Fore.GREEN}Well done! {guess} is in the word.{Fore.RESET}'
        else:
            remaining_attempts -= 1
            result_message = f'{Fore.RED}Unlucky! {guess} is not in the word{Fore.RESET}'
        
        if '_' not in display:
            print(winner_ascii)
            print(f'{Fore.YELLOW}\nCongratulations! You win!{Fore.RESET}')
            break
            # bug upon winning. requires another input to 
            # display winning message and break

        if remaining_attempts == 0:
            print(f'{Fore.RED}\nYou lost the game, the word is {hidden_word}.{Fore.RESET}')
            break

        # add reset or quit game function

main_menu()