#File: HangmanTests.py

from HangmanFunctions import *
from os import remove
from os import system

def wordReadingTest():
    fileName = "wordsForTest.txt"
    wordsForTest = open(fileName, "w")
    wordsForTest.write("chose\nessai\nmot\ntest")
    wordsForTest.close()
    wordList = readWordFile(fileName)
    remove(fileName)
    word = str()
    try:
        word = wordList[0]
        assert(word=="chose")
    except AssertionError:
        print("Error: wordList[0] = {0}".format(word))
    try:
        word = wordList[1]
        assert(word=="essaie")
    except AssertionError:
        print("Error: wordList[1] = {0}".format(word))
    try:
        word = wordList[2]
        assert(word=="mot")
    except AssertionError:
        print("Error: wordList[2] = {0}".format(word))
    try:
        word = wordList[len(wordList)-1]
        assert(word=="test")
    except AssertionError:
        print("Error: last word list = {0}".format(word))

def testAll():
    wordReadingTest()

if __name__ == "__main__":
    testAll()
    system("pause")
