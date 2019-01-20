#File: MysteryWordGame

from os import system
from random import randint

def eliminateCharacter(index, aString):
    beginning = aString[0:index]
    end = aString[index+1:]
    return beginning + end

def mixCharacters(aString):
    strToMix = aString
    mixedStr = ""
    while len(strToMix) > 0:
        randIndex = randint(0, len(strToMix)-1)
        mixedStr = mixedStr + strToMix[randIndex]
        strToMix = eliminateCharacter(randIndex, strToMix)
    return mixedStr

def newLines(nb):
    i = 0
    while i < nb:
        print("")
        i += 1

def playGame():
    answer = ""
    mixedWord = ""
    wordToGuess = input("Enter a word to guess: ").upper()
    print("Word to guess: ", wordToGuess, ".")
    newLines(53)
    while True:
        mixedWord = mixCharacters(wordToGuess)
        print("Mixed letters: ", mixedWord, ".")
        answer = input("Your answer: ").upper()
        if answer == wordToGuess:
            print(answer, " is the good answer.\n")
            break;
        else:
            print(answer, "is a wrong answer.\n")

playGame()
system("pause")
