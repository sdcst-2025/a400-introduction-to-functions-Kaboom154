"""
Create a program with 3 function definitions:
function A prints the message "Hello"
function B prints the message "How are you"
function C prints the message "Hi"

Ask the user to enter a letter from A to C
Execute the function of the letter they use.
"""

def A():
    print('Hello')

def B():
    print('How are you')

def C():
    print('Hi')

num = input('Enter a number from A to C: ')
if num in ['A','a']:
    A()
if num in ['B','b']:
    B()
if num in ['C','c']:
    C()