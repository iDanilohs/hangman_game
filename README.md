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

```python
    os.system("clear")
    # Select a word
    aleatory_number = random.randint(1, 172)
    words = []
    with open("./data.txt", "r", encoding="utf-8") as f:
        for line in f:
            words.append(str(line))

    select_word = words[aleatory_number]
    select_word = select_word.replace('\n', '')
```

In this part of the code we clear the screen and select a random number. This number will be used to select a random word from the file.txt in this case (data.txt).

also we create a new list (words = []) for read the archive, I mean put all of the words in the list  for then can combine the list words with the random number and create the variable (select_word) and for last we clean the word, I mean remove the unuseful spaces in the word (select word).

```python
    letter_by_letter = list(select_word)
    count_letter = 0
    for letter in letter_by_letter:
        count_letter += 1 
```

continuing in this part of the code by counting the letters of the word, using a (for loop), which reads letter by letter from the variable (select_word) and returns the number to be stored in the varible (count_letter)