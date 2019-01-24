# File: PythonTests.py

from os import system
import CustomFunctions

year = input("Enter a year: ")
year = int(year)

try:
        if CustomFunctions.isLeapYear(year):
                print(year, "is a leap year.\n")
        else:
                print(year, "is not a leap year.\n")
except ValueError as ve:
        print(ve, "\n")

a = input("Enter integer a: ")
a = int(a)
b = input("Enter integer b: ")
b = int(b)
print("Greatest common divider: {0}\n".format(CustomFunctions.greatestCommonDivider(a, b)))

c = input("Enter integer c: ")
c = int(c)
d = input("Enter integer d: ")
d = int(d)
print("Least common multiple: {0}\n".format(CustomFunctions.leastCommonMultiple(c, d)))

system("pause")
