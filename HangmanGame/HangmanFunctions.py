#File: HangmanFunctions.py

from HangmanData import scoreFileName, wordFileName
from pickle import Pickler, Unpickler
from random import randint

def getScoreDictionary(fileName):
    scoreDict = None
    try:
        with open(fileName, "rb") as scoreFile:
            scoreUnpickler = Unpickler(scoreFile)
            scoreDict = scoreUnpickler.load()
    except FileNotFoundError:
        pass
    return scoreDict

def initScoreFile(force=False):
    if force or getScoreDictionary(scoreFileName) is None:
        saveScoreDictionary({}, scoreFileName)

def randomWord():
    wordList = readWordFile(wordFileName)
    return wordList[randint(0, len(wordList)-1)]

def readWordFile(fileName):
    wordFile = open(fileName, "r")
    words = wordFile.read()
    wordList = words.split("\n")
    wordFile.close()
    return wordList

def saveScoreDictionary(scoreDict, fileName):
    with open(fileName, "wb") as scoreFile:
        scorePickler = Pickler(scoreFile)
        scorePickler.dump(scoreDict)

def updateScore(name, points):
    currentScore = 0
    scoreDict = getScoreDictionary(scoreFileName)
    if scoreDict is None:
        scoreDict = dict()
    else:
        try:
            currentScore = scoreDict[name]
        except KeyError:
            pass #New player. The current score is still 0.
    scoreDict[name] = currentScore + points
    saveScoreDictionary(scoreDict, scoreFileName)

if __name__=="__main__":
    from os import system
    #saveScoreDictionary({"joueurA": 2, "joueurB": 3}, scoreFileName)
    #initScoreFile(True)
    #updateScore("joueur1", 4)
    #updateScore("joueur2", 7)
    print(getScoreDictionary(scoreFileName))
    #print(randomWord())
    system("pause")
