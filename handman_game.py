import random
    

def run():
    aleatory_number = random.randint(1, 172)
    words = []
    with open("./data.txt", "r", encoding="utf-8") as f:
        for line in f:
            words.append(str(line))
    print(words)


if __name__ == '__main__':
    run()