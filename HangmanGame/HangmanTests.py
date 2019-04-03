#File: HangmanTests.py

from HangmanFunctions import *
from os import system

def wordReadingTest():
    wordList = readWordFile("words.txt")
    word = str()
    try:
        word = wordList[0]
        assert(word=="armoire")
    except AssertionError:
        print("Error: wordList[0] = {0}".format(word))
    try:
        word = wordList[1]
        assert(word=="boucle")
    except AssertionError:
        print("Error: wordList[1] = {0}".format(word))
    try:
        word = wordList[2]
        assert(word=="buisson")
    except AssertionError:
        print("Error: wordList[2] = {0}".format(word))
    try:
        word = wordList[len(wordList)-1]
        assert(word=="volant")
    except AssertionError:
        print("Error: last word list = {0}".format(word))

def testAll():
    wordReadingTest()

if __name__ == "__main__":
    testAll()
    system("pause")
