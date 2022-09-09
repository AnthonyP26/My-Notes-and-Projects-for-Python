import random

winner  = False

wordList = ["accident", "baseball", "cucumber", "broccoli", "keyboard", "recorder", "goldfish", "reindeer"]
word = random.choice(wordList)
word = [*word]
letterList = ["-", "-", "-", "-", "-", "-", "-", "-"]
wrongAnswers = 0
def turnFunc():
    global word
    global letterList
    global winner
    global wrongAnswers
    print(word)

    
    while wrongAnswers != 56 and winner == False:
        hangMan()

        #if wrongAnswers == 0:
            #hangMan()
        #elif wrongAnswers == 8:
        #    hangMan1()
        #elif wrongAnswers == 16:
        #    hangMan2()
        #elif wrongAnswers == 24:
        #    hangMan3()
        #elif wrongAnswers == 32:
        #    hangMan4()
        #elif wrongAnswers == 40:
        #    hangMan5()
        #elif wrongAnswers == 48:
            #hangMan6()
        
        if wrongAnswers == 40:
            print("You Died")
            break
        elif letterList[0:8] == word[0:8]:
            print("You Win!")
            winner = True

        inp = input("Guess: ")
        inp.lower()
        for i in range(len(word)):
            if inp == word[i]:
                letterList[i] = inp
                continue
            else:
                wrongAnswers += 1
                continue

def hangMan():
    print(" ______________________")
    print("|                      |")
    print("|                      |")
    print("|                      |")
    print("|                      |")
    print("|                      |")
    print("|                      |")
    print("|                      |")
    print("|                      |")
    print("|   ", letterList[0], letterList[1], letterList[2], letterList[3], letterList[4], letterList[5], letterList[6], letterList[7], "  |")
    print("|______________________|")


def hangMan1():
    print(" ______________________")
    print("|         _____        |")
    print("|        |     |       |")
    print("|        |_____|       |")
    print("|                      |")
    print("|                      |")
    print("|                      |")
    print("|                      |")
    print("|                      |")
    print("|   ", letterList[0], letterList[1], letterList[2], letterList[3], letterList[4], letterList[5], letterList[6], letterList[7], "  |")
    print("|______________________|")


def hangMan2():
    print(" ______________________")
    print("|         _____        |")
    print("|        |     |       |")
    print("|        |_____|       |")
    print("|           |          |")
    print("|           |          |")
    print("|                      |")
    print("|                      |")
    print("|                      |")
    print("|   ", letterList[0], letterList[1], letterList[2], letterList[3], letterList[4], letterList[5], letterList[6], letterList[7], "  |")
    print("|______________________|")

def hangMan3():
    print(" ______________________")
    print("|         _____        |")
    print("|        |     |       |")
    print("|        |_____|       |")
    print("|           |          |")
    print("|           |          |")
    print("|          /           |")
    print("|         /            |")
    print("|                      |")
    print("|   ", letterList[0], letterList[1], letterList[2], letterList[3], letterList[4], letterList[5], letterList[6], letterList[7], "  |")
    print("|______________________|")

def hangMan4():
    print(" ______________________")
    print("|         _____        |")
    print("|        |     |       |")
    print("|        |_____|       |")
    print("|           |          |")
    print("|           |          |")
    print("|          / \         |")
    print("|         /   \        |")
    print("|                      |")
    print("|   ", letterList[0], letterList[1], letterList[2], letterList[3], letterList[4], letterList[5], letterList[6], letterList[7], "  |")
    print("|______________________|")

def hangMan5():
    print(" ______________________")
    print("|         _____        |")
    print("|        |     |       |")
    print("|        |_____|       |")
    print("|           |-----     |")
    print("|           |          |")
    print("|          / \         |")
    print("|         /   \        |")
    print("|                      |")
    print("|   ", letterList[0], letterList[1], letterList[2], letterList[3], letterList[4], letterList[5], letterList[6], letterList[7], "  |")
    print("|______________________|")

def hangMan6():
    print(" ______________________")
    print("|         _____        |")
    print("|        |     |       |")
    print("|        |_____|       |")
    print("|      -----|-----     |")
    print("|           |          |")
    print("|          / \         |")
    print("|         /   \        |")
    print("|                      |")
    print("|   ", letterList[0], letterList[1], letterList[2], letterList[3], letterList[4], letterList[5], letterList[6], letterList[7], "  |")
    print("|______________________|")

turnFunc()