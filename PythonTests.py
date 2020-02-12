# File: PythonTests.py

from os import system
import CustomFunctions

floatNbr = 3.999999999
print("{0} will be converted to a string.".format(floatNbr))
print("Precision -1: {0}".format(CustomFunctions.floatNumberToString(floatNbr, -1)))
print("Precision 0: {0}".format(CustomFunctions.floatNumberToString(floatNbr)))
print("Precision 1: {0}".format(CustomFunctions.floatNumberToString(floatNbr, 1)))
print("Precision 3: {0}".format(CustomFunctions.floatNumberToString(floatNbr, 3)))
print("Precision 5: {0}".format(CustomFunctions.floatNumberToString(floatNbr, 5)))

floatNbr = 11.0
print("\n{0} will be converted to a string.".format(floatNbr))
print("Precision 0: {0}".format(CustomFunctions.floatNumberToString(floatNbr)))
print("Precision 1: {0}".format(CustomFunctions.floatNumberToString(floatNbr, 1)))
print("Precision 2: {0}".format(CustomFunctions.floatNumberToString(floatNbr, 2)))

year = input("\nEnter a year: ")
year = int(year)

try:
        if CustomFunctions.isLeapYear(year):
                print(year, "is a leap year.")
        else:
                print(year, "is not a leap year.")
except ValueError as ve:
        print(ve)

a = input("\nEnter integer a: ")
a = int(a)
b = input("Enter integer b: ")
b = int(b)
print("Greatest common divisor of a and b: {0}".format(CustomFunctions.greatestCommonDivisor(a, b)))

c = input("\nEnter integer c: ")
c = int(c)
d = input("Enter integer d: ")
d = int(d)
print("Least common multiple of c and d: {0}".format(CustomFunctions.leastCommonMultiple(c, d)))

position = input("\nCalculate the Fibonacci number at position: ")
position = int(position)
try:
        fibonacciNumber = CustomFunctions.fibonacci(position)
        print("Term {0} of the Fibonacci sequence is {1}.\n".format(position, fibonacciNumber))
except ValueError as ve:
        print("{0}\n".format(ve))

system("pause")
