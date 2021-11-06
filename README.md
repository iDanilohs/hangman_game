# Description
This is a game for guess the word randomly selected by the computer for you, and you have 6 lives to get it right.

# Skills
- list comprenhension.
- loops.
- File management.
- Assetment.
- Conditionals.

# Hangman_game

![](https://i.imgur.com/Hk6ovKt.png)

![](https://img.shields.io/badge/python-3.9-green)


# Documentation.
first we need 2 modules from python native, random and OS. Now, how can import this modules? with an import function at the top of the code.
```python
import random
import os
```
second we need the basic structure for run the code in the terminal, then we write the following:
```python
import random
import os


def run():
	pass


if __name__ == '__main__':
    run()
```
third step we import or [make the message](http://patorjk.com/software/taag/#p=display&h=2&v=2&f=Big&t=you%20loss%20 "make the message") to win or lose and we also import the graphics for the [hangman animation.](http://gist.github.com/chrishorton/8510732aa9a80a03c829b09f12e20d9c "hangman animation.") Then we put the graphics and the messages inside the function run() in the following way:
```python
import random
import os


def run():
	WIN = [
        '''
        
 __     __                    _       
 \ \   / /                   (_)      
  \ \_/ /__  _   _  __      ___ _ __  
   \   / _ \| | | | \ \ /\ / / | '_ \ 
    | | (_) | |_| |  \ V  V /| | | | |
    |_|\___/ \__,_|   \_/\_/ |_|_| |_|
                                      
                                      

        ''',
        '''
        
                      _                
                     | |               
  _   _  ___  _   _  | | ___  ___ ___  
 | | | |/ _ \| | | | | |/ _ \/ __/ __| 
 | |_| | (_) | |_| | | | (_) \__ \__ \ 
  \__, |\___/ \__,_| |_|\___/|___/___/ 
   __/ |                               
  |___/                                

        '''
    ]

    HANGMANPICS = ['''
  +---+  lives:  ❤️ ❤️ ❤️ ❤️ ❤️ ❤️
  |   |
      |
      |
      |
      |
=========''', '''
  +---+  lives: ❤️ ❤️ ❤️ ❤️ ❤️
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+  lives: ❤️ ❤️ ❤️ ❤️
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+  lives: ❤️ ❤️ ❤️
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+  lives: ❤️ ❤️
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+  lives: ❤️
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+  You died 
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


if __name__ == '__main__':
    run()
```

Let's look at the logic before the game loop.

![](https://i.imgur.com/la6Us8L.png)