import random
import os

def run():
    os.system("clear")
    aleatory_number = random.randint(1, 172)
    words = []
    with open("./data.txt", "r", encoding="utf-8") as f:
        for line in f:
            words.append(str(line))

    select_word = words[aleatory_number]
    select_word = select_word.replace('\n', '')
    letter_by_letter = list(select_word)
    count_letter = 0
    for letter in letter_by_letter:
        count_letter = count_letter + 1 


    show = []
    for i in range(0, count_letter):
        show.append("_")

    count_time = 0

    while count_letter > count_time:
        user = str(input("\n Escribe una letra: "))
        count = -1
        for i in select_word:
            count = count + 1
            if i == user:
                show[count] = user
                count_time = count_time + 1
            else:
                continue

        # print(show)
        print(select_word)
        # print("Contador de letras", count_letter)
        for i in range(0, count_letter):
            print(show[i], end=" ")
        print("\n Tu letra ateriror fue ", user)
        # print("contador de tiempos", count_time)
    print("Ganaste Felicidades :)")
    
    


if __name__ == '__main__':
    run()