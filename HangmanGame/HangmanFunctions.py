#File: HangmanFunctions.py

def readWordFile(fileName):
    wordFile = open(fileName, "r")
    words = wordFile.read()
    wordList = words.split("\n")
    wordFile.close()
    return wordList
