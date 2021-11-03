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

    ubications = []
    count_ubication = 0
    for ubi in ubications:
        count_ubication = count_ubication + 1

    while count_ubication != count_letter:
        user = str(input("Escribe una letra: "))
        count = -1
        for i in select_word:
            count = count + 1
            if i == user:
                ubications.append(count)
            else:
                continue
        print(ubications)
    
    


if __name__ == '__main__':
    run()