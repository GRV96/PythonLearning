#File: HangmanFunctions.py

#import HangmanData
from random import randint

def randomWord():
    wordList = readWordFile("words.txt")
    return wordList[randint(0, len(wordList)-1)]

def readWordFile(fileName):
    wordFile = open(fileName, "r")
    words = wordFile.read()
    wordList = words.split("\n")
    wordFile.close()
    return wordList
