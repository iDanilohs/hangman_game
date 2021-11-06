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

    os.system("clear")
    # Select a word
    aleatory_number = random.randint(1, 172)
    words = []
    with open("./data.txt", "r", encoding="utf-8") as f:
        for line in f:
            words.append(str(line))

    select_word = words[aleatory_number]
    select_word = select_word.replace('\n', '')

    #become and counting letters of the word
    letter_by_letter = list(select_word)
    count_letter = 0
    for letter in letter_by_letter:
        count_letter += 1 

    #The list of the user
    # show = []
    # for i in range(0, count_letter):
    #     show.append("_")
    show = [("_") for i in range(0, count_letter)]

    lives = 0

    # Big loop for a game
    # while count_letter > count_time:
    while show != letter_by_letter:
        os.system("clear")
        #read spaces
        for i in range(0, count_letter):
            print(show[i], end=" ")

        #show image, we request letter
        found = False
        count = -1
        print(HANGMANPICS[lives])
        # print(select_word)
        user = str(input("\n Write one letter: "))

        #Compare letters
        for i in select_word:
            count += 1
            if i == user:
                show[count] = user
                found = True
            else:
                continue
        if not found:
            lives += 1

        if lives == 6:
            break

        #For errors
        proof = user.isdigit()
        assert len(user) > 0, "Debes poner una letra por lo menos"
        assert proof == False, "Tienes que poner letras no números"
        assert len(user) < 2, "Solamente debes poner una letra"
        
        
    if lives == 6:
        os.system("clear")
        print(WIN[1])
        print("The word was: ",select_word)
    else:
        os.system("clear")
        print(WIN[0])
        print("The word was: ",select_word)


if __name__ == '__main__':
    run()