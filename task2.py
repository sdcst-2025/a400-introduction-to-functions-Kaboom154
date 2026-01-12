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
def title():
    system('clear||cls')
    print('The computer will generate a random number, and you must try to guess what it is.')
    time.sleep(1)
    print('The computer will tell you if you are above or below the number')
    time.sleep(1)
    num = input('To start the game, press 1')
    if num == '1' 

title()