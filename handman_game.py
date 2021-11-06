import random
import os


def run():
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

    count_time = 0

    # Big loop for a game
    # while count_letter > count_time:
    while show != letter_by_letter:
        
        user = str(input("\n Escribe una letra: "))
        proof = user.isdigit()
        assert len(user) > 0, "Debes poner una letra por lo menos"
        assert proof == False, "Tienes que poner letras no números"
        assert len(user) < 2, "Solamente debes poner una letra"
        count = -1
        for i in select_word:
            count += 1
            if i == user:
                show[count] = user
                count_time += 1
            else:
                continue

        # print(show)
        print(select_word)
        # print("Contador de letras", count_letter)
        for i in range(0, count_letter):
            print(show[i], end=" ")
        print("\n Tu letra ateriror fue ", user)
        # print("contador de tiempos", count_time)
        

    os.system("clear")
    print("Ganaste Felicidades :)")
    
    


if __name__ == '__main__':
    run()