# This roulette game is an exercise available on this site:
# https://openclassrooms.com/fr/courses/235344-apprenez-a-programmer-en-python/231735-tp-tous-au-zcasino

from math import ceil
from os import system
from random import randint

amount = 10000

while amount > 0:
    # Player information and input
    print("Available amount:", amount, "$")
    stake = int(input("Your stake (0 to stop): "))
    if stake <= 0:
        print("")
        break
    bet = int(input("Your bet (0 to 49): "))

    # The game
    winningNumber = randint(0, 49)
    print("Winning number:", winningNumber)
    if bet == winningNumber:
        price = 3 * stake
        amount += price
        print("You won", price, "$!\n")
    elif bet%2 == winningNumber%2:
        price = ceil(stake / 2)
        amount += price
        print("You won", price, "$!\n")
    else:
        amount -= stake
        print("You lost.\n")
print("You leave the casino with", amount, "$.")
system("pause")
