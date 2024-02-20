import random
import os
from colorama import Fore, init
from words import list_of_words
from ascii import (
    splash_screen,
    winner_ascii,
    loser_ascii,
    quit_ascii,
    hangman_stages
)

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
            print('Press 1 to start game')
            print('press 2 to read instructions\n')

            options = (input('Enter your choice here: '))

            if options == '1':
                clear_screen()
                run_game()
                break
            elif options == '2':
                clear_screen()
                instructions()
                break
            else:
                raise ValueError(
                    f'{Fore.RED}Only 1 or 2 are allowed, '
                    f'try again.{Fore.RESET}'
                    )

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
    print('It is to guess what the hidden word is '
          'before the stick figure is hung.\n')
    print('Start guessing letters when prompted')
    print('Choose your guesses wisely, you have 7 lives!\n')
    print('The game ends when you either guess the correct word '
          'or you run out of lives.\n')

    try:
        print('Press 1 to start game')
        print('press 2 for main menu')
        print('Press 3 to quit\n')

        start_game = input('Enter your choice here: ')

        if start_game == '1':
            clear_screen()
            run_game()
        elif start_game == '2':
            clear_screen()
            main_menu()
        elif start_game == '3':
            clear_screen()
            print(quit_ascii)
        else:
            raise ValueError(
                f'{Fore.RED}Invalid input. '
                f'Press 1 to go start game.\n{Fore.RESET}')
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
            display += letter + ' '
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
            raise ValueError(
                f'{Fore.RED}Only single letters allowed.{Fore.RESET}')

        if guess in guessed_letter_list:
            raise ValueError(
                f'{Fore.RED}You have already guessed this letter. '
                f'Try again.{Fore.RESET}')
        else:
            guessed_letter_list.append(guess)

        return guess
    except ValueError as e:
        print(e)
        return guessed_letter()


def reset_game():
    """
    resets the game upon user input
    """
    clear_screen()
    global remaining_attempts
    global guessed_letter_list
    remaining_attempts = 7
    guessed_letter_list = []
    run_game()


def quit_game():
    """
    Quits the game and prints a thank you
    for playing message upon user input
    """
    clear_screen()
    print(quit_ascii)


def run_game():
    """
    Runs the game logic
    """
    remaining_attempts = 7
    hidden_word = get_word()
    result_message = ''

    # Displays the game as long as user has not won or lost
    while remaining_attempts > 0:
        clear_screen()
        print('Lets play!\n')
        print(f'Lives: {remaining_attempts}\n')
        print('Guessed Letters: ' + ' '.join(guessed_letter_list))
        print(result_message)
        print(hangman_stages(remaining_attempts))

        display = display_word(hidden_word, guessed_letter_list)
        print(f'{display}\n')

        guess = guessed_letter()

        # Checks whether user guessed correctly or incorrectly
        # Displays message to tell user
        # and adjusts remaining attempts accordingly
        if guess in hidden_word:
            result_message = (
                f'{Fore.GREEN}Well done! {guess} is in the word.{Fore.RESET}'
                )
        else:
            remaining_attempts -= 1
            result_message = (
                f'{Fore.RED}Unlucky! {guess} is not in the word{Fore.RESET}'
            )

        display = display_word(hidden_word, guessed_letter_list)

        # Checks if user won
        # Gives user option to restart or quit if true
        if '_' not in display:
            clear_screen()
            print(winner_ascii)
            play_again = input(
                'Press 1 to play again or press any key to quit: '
                    )
            if play_again == '1':
                reset_game()
            else:
                return quit_game()
            # bug upon winning. requires another input to print winner ascii

        # Checks if user lost
        # Gives user option to restart or quit if true
        if remaining_attempts == 0:
            clear_screen()
            print(loser_ascii)
            print(f'{Fore.RED}\nThe word is {hidden_word}.{Fore.RESET}')
            play_again = input(
                'Press 1 to play again or press any key to quit: '
                    )
            if play_again == '1':
                reset_game()
            else:
                return quit_game()


# Calls the main menu. Everything else is called from main menu
main_menu()
