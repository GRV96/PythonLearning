# File: PythonTests.py

from os import system
import CustomFunctions

year = input("Enter a year: ")
year = int(year)

if CustomFunctions.isLeapYear(year):
	print(year, "is a leap year.\n")
else:
	print(year, "is not a leap year.\n")

a = input("Enter integer a: ")
a = int(a)
b = input("Enter integer b: ")
b = int(b)
print("Greatest common divider: ", CustomFunctions.gcdEuclid(a, b))

system("pause")
