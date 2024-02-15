import random
from words import list_of_words

def introduction():
    """
    Welcomes the user and explains the rules
    """
    print('Thank you for choosing to play Hangman!\n')
    print('The objective of the game is simple!\n')
    print('It is to guess the what the hidden word is before the stick figure is hung.\n')
    print('Start guessing letters when prompted')
    print('Choose your letters wisely, you have 8 lives!\n')
    print('The game ends when you either guess the correct word or you run out of lives.\n')
    
    start_game = input('Type "start" to begin game: ')

    if start_game != 'start':
        print('Invalid input. Type "start" to begin game')
    

def get_word():
    """
    Generates a random word from the list_of_words.
    """
    word = random.choice(list_of_words)
    return word

def display_word(word, user_input):
    """
    Displays hidden letters in hidden word as underscores
    and reveals letters that are guessed correctly
    """            

def main():
    introduction()
    get_word()

main()         
