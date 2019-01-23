# This roulette game is an exercise available on this site:
# https://openclassrooms.com/fr/courses/235344-apprenez-a-programmer-en-python/231735-tp-tous-au-zcasino

from math import ceil
from os import system
from random import randint

amount = 10000

while amount > 0:
    # Player information and input
    print("Available amount: {0}$".format(amount))
    stake = int(input("Your stake (0 to stop): "))
    if stake <= 0:
        print("")
        break
    bet = int(input("Your bet (0 to 49): "))

    # The game
    winningNumber = randint(0, 49)
    print("Winning number: {0}".format(winningNumber))
    if bet == winningNumber:
        price = 3 * stake
        amount += prize
        print("You won {0}$!\n".format(prize))
    elif bet%2 == winningNumber%2:
        prize = ceil(stake / 2)
        amount += prize
        print("You won {0}$!\n".format(prize))
    else:
        amount -= stake
        print("You lost.\n")
print("You leave the casino with {0}$.".format(amount))
system("pause")
