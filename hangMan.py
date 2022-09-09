import random
from re import I
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
    
    while winner == False:
        print(wrongAnswers)
        if 40 == wrongAnswers:
            hangMan5()
        elif 32 == wrongAnswers:
            hangMan4()
        elif 24 == wrongAnswers:
            hangMan3()
        elif 16 == wrongAnswers:
            hangMan2()
        elif 8 == wrongAnswers:
            hangMan1()
        else:
            hangMan()

        if wrongAnswers == 48:
            hangMan6()
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
        if inp not in word:
            wrongAnswers += 8
            

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
