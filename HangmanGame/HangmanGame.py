#File: HangmanGame.py

from HangmanData import chances
from HangmanFunctions import randomWord, updateScore
from os import system

wordToGuess = randomWord()
letterCount = len(wordToGuess)
playerName = input("Enter your name: ")
rightLetterCount = 0
wrongLetters = []

#Initialize the list containing the found letters
foundLetters = list()
i = 0
while i<letterCount:
    foundLetters.append("_")
    i += 1

def updateFoundLetters(letter):
    correctLetters = 0
    lastOccurence = -1
    while True:
        try:
            letterIndex = wordToGuess.index(letter, lastOccurence+1)
            lastOccurence = letterIndex
            foundLetters[letterIndex] = letter
            correctLetters += 1 #Never reached if an exception is raised
        except ValueError:
            break
    return correctLetters

#Play the game
while chances>0 and rightLetterCount<letterCount:
    print("\nWrong letters: " + " ".join(wrongLetters))
    print("You have {0} chances left.".format(chances))
    print(" ".join(foundLetters))
    letter = input("Try a letter: ")[0]
    correctLetters = updateFoundLetters(letter)
    if correctLetters>0:
        rightLetterCount += correctLetters
    else:
        wrongLetters.append(letter)
        chances -= 1

#Game result
if chances>0:
    print("\nYou guessed the word! You earned {0} points.".format(chances))
    updateScore(playerName, chances)
else:
    print("\nYou lost. The word to guess was {}.".format(wordToGuess))

system("pause")
