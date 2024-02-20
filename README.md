# Project Portfolio 3: Hangman

My Hangman game is a Python terminal game that runs on Heroku. The aim of the game is to guess the hidden word before the hangman image is completed. This game is targeted at people of any ages, who want to engage in a quick brainteaser.

* Find the link to the game [here](https://hangman-pp3-2024-2fbba5f87d9d.herokuapp.com/)
* The repository link is [here](https://github.com/PaulR1209/hangman)

## How to Play

1. To start, there will be a hidden word displayed as underscores, with with an image of the Hangman, and the amount of lives you have. This hidden word is chosen at random from my words.py file. I was able to execute this by importing the random library.
2. You will be prompted to guess a letter.
3. If you guess correctly, the letter will be revealed in the relevant space. If you guess wrong, the hangman image will progress to the next stage, and you will lose a life.
4. You win by guessing all letters correctly.
5. If you run out of lives, and the hangman image is completed, you will lose the game.
6. Upon win or lose you will be greeted with the relevant message and will be prompted to either restart the game, or quit.

## Game Design

<img src='/screenshots/flow-chart.png'>

## Features

### Main Menu

The main menu consists of a hangman logo ascii art, which has added color. To do this, I imported the Colorama library into my workspace.

At the bottom you can choose to either start the game or read the instructions, by pressing either 1 or 2.

<img src='/screenshots/main-menu.png'>

#### Main Menu Error

If you press any other key other than 1 or 2, an error is thrown and a message to the user is displayed in red at the top.

I have color coded all of my errors to red, so it catches the users eye.

<img src='/screenshots/main-menu-error.png'>

### Instructions

This is the instructions for the game. The user can either press 1 to start the game once they are finished reading, or press 2 to go back to the main menu, or press 3 to quit, which will take you to the quit screen referenced further down.

<img src='/screenshots/instructions.png'>

#### Instructions Error

This error is displayed upon pressing any other key, other than 1, 2 or 3.

<img src='/screenshots/instructions-error.png'>

### Game

#### Start Screen

This is the opening display when you start the game:

After every input, the screen clears and refreshes. I imported the OS library in order that I could use my clear screen function.

* Remaining lives
* A list of guessed letters, which is currently empty
* The Hangman image, which updates every time you lose a life.
* The hidden word, which is displayed as underscores, and then gets revealed when letters are guessed correctly.
* User input

<img src='/screenshots/start-game.png'>

#### Correct Guess

When user guesses correctly, the letter is revealed in the word, and a green message pops up confirming the letter is in the word.

<img src='/screenshots/correct-guess.png'>

#### Incorrect Guess

When user guesses incorrectly, the remaining lives go down, the hangman image updates, and you get a red message to confirm the letter is not in the word.

<img src='/screenshots/incorrect-guess.png'>

#### Invalid User Inputs

When the user types in more than one character, or a key that is not a letter, or the letter has already been guessed, user will get one of two error messages.

<img src='/screenshots/game-error.png'>

<img src='/screenshots/already-guessed.png'>

#### Game Result

Upon winning or losing, the user is greeted with a message to confirm result, and is prompted to either restart game, or quit.

When you lose, the hidden word will be revealed in red so user can clearly see.

<img src='/screenshots/win.png'>

<img src='/screenshots/lose.png'>

#### Quit Screen

Upon choosing to quit, user is greeted with a thank you for playing message.

<img src='/screenshots/game-over.png'>

## Technologies

* This game is all written in Python
* The IDE used is Gitpod with Code Institute template
* I used Heroku to deploy my project
* Git has been used to commit, push and store to GitHub
* I used [This Webiste](https://patorjk.com/software/taag/#p=display&h=0&f=Doom&t=Hangman) to generate my ascii art messages.
* I used ChatGPT to generate ascii art for my Hangman images

## Testing

Throughout writing this project, I regularly used the terminal to test my code. Everything currently works as expected.

What I tested:

* In main menu and Instructions menu, I made sure I was able to move around, based on my menu choices.
* I used invalid inputs to check if my error messaged were working, and if any unexpected errors came up.
* When running the game, I checked for invalid inputs and unexpected errors the same as previous.
* I played the game to win, to make sure the messages to the user were appearing, the letters had been revealed in the hidden word, and the winning message came up.
* I then played to lose, to check if my lives were going down, the hangman stages were progressing, and the losing message came up.
* Upon being prompted to either restart or quit, I again checked for errors by inputting an invalid key, and checked if the game would properly restart, and the game would move to the quit screen.
* Finally upon putting my code through a validator, I manually edited my code to make it PEP8 standard.

### Validator

I ran my code through Code Institute Python Linter with no errors.

<img src='/screenshots/validator.png'>

## Bugs

Although I have no bugs I am aware of, I did have a problem, where upon winning, guessing all letters in the word, I would have to input one more guess in order to display the winning screen.

With help from my mentor, I discovered that I was not checking the hidden word after the user input, so when checking for a winner, it was not picking up that I had won.

<img src='/screenshots/bug.png'>

## Deployment

I deployed my project to Heroku by following these steps:

1. I created an account with Heroku
2. I then clicked 'Create new app'
3. I went into settings, and added Python and Node.js buildpacks in that order
4. Then I connected my Github profile and selected my repository.
5. Finally I deployed my page and enabled automatic deploys

## Credits

* I used https://codefather.tech/blog/hangman-game-python/ to understand the basic structure of a hangman game and took some inspiration from his code.
* I used ChatGPT to write the clear screen function and also used this to get colorama working