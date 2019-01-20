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
    wordToGuess = input("Enter a word to guess: ").upper()
    print("Word to guess: ", wordToGuess, ".")
    mixedWord = ""
    answer = ""
    while True:
        newLines(53)
        mixedWord = mixCharacters(wordToGuess)
        print("Mixed letters: ", mixedWord, ".")
        answer = input("Your answer: ").upper()
        if answer == wordToGuess:
            print(answer, " is the good answer.")
            break;
        else:
            print(answer, "is a wrong answer.")
            system("pause")

playGame()
system("pause")
