# Project Portfolio 3: Hangman

My Hangman game is a Python terminal game that runs on Heroku. The aim of the game is to guess the hidden word before the hangman image is completed.

* Find the link to the game [here](https://hangman-pp3-2024-2fbba5f87d9d.herokuapp.com/)
* The repository link is [here](https://github.com/PaulR1209/hangman)

## How to Play

1. To start, there will be a hidden word displayed as underscores, with with an image of the Hangman, and the amount of lives you have.
2. You will be prompted to guess a letter.
3. If you guess correctly, the letter will be revealed in the relevant space. If you guess wrong, the hangman image will progress to the next stage, and you will lose a life.
4. You win by guessing all letters correctly.
5. If you run out of lives, and the hangman image is completed, you will lose the game.
6. Upon win or lose you will be greeted with the relevant message and will be prompted to either restart the game, or quit.

## Game Design

<img src='/screenshots/flow-chart.png'>

## Features

### Main Menu

The main menu consists of a hangman logo ascii art, which has added color. To do this, I imported Colorama into my workspace.

At the bottom you can choose to either start the game or read the instructions, by pressing either 1 or 2.

<img src='/screenshots/main-menu.png'>

#### Main Menu Error

If you press any other key other than 1 or 2, an error is thrown and a message to the user is displayed in red at the top.

I have color coded all of my errors to red, so it catches the users eye.

<img src='/screenshots/main-menu-error.png'>

### Instructions

This is the instructions for the game. The user can press 1 to start the game once they are finished reading.

<img src='/screenshots/instructions.png'>

#### Instructions Error

This error is displayed upon pressing any other key, other than 1.

<img src='/screenshots/instructions-error.png'>

