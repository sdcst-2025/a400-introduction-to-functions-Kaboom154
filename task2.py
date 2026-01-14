"""
Create a program to play a number guessing game
There should be a function:
title()
displays instructions and how to play

game()
plays the game

This will be silimar to something you have already done, but in this task you 
are breaking the code up into different sections to make each a function.
"""
from os import system
import time
import random

def title():
    system('clear||cls')
    print('The computer will generate a random number, and you must try to guess what it is.')
    time.sleep(1)
    print('The computer will tell you if you are above or below the number')
    time.sleep(0.5)
    num = input('To start the game, press 1: ')
    if num == '1':
        game()
    else: 
        title()

def game():
    system('clear||cls')
    guess = 0
    randnum = random.randint(1,100)
    count = 0
    while guess != randnum:
        guess = int(input('guess a number between 1 and 100: '))
        if guess > randnum: 
            print('Too high')
        if guess < randnum: 
            print('Too low')
        count += 1
    if guess == randnum:
        print(f'You guessed the correct number in {count} tries')
        playAgain = input('To play again, press 1: ')
        if playAgain == '1':
            game()
title()