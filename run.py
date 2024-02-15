import random
from words import list_of_words

def get_word():
    word = random.choice(list_of_words)
    print(word)

get_word()     
