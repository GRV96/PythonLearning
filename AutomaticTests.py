#File: AutomaticTests.py

from CustomFunctions import *
from os import system

def fibonacciTest():        
    try:
        testResult = fibonacci(-1)
    except ValueError:
        pass #Expected. Do nothing.

    try:
        testOutput = fibonacci(0)
        assert testOutput==0
    except AssertionError:
        print("Test fibonacci(0) failed. Output: {0}.".format(testOutput))

    try:
        testOutput = fibonacci(1)
        assert testOutput==1
    except AssertionError:
        print("Test fibonacci(1) failed. Output: {0}.".format(testOutput))

    try:
        testOutput = fibonacci(2)
        assert testOutput==1
    except AssertionError:
        print("Test fibonacci(2) failed. Output: {0}.".format(testOutput))

    try:
        testOutput = fibonacci(3)
        assert testOutput==2
    except AssertionError:
        print("Test fibonacci(3) failed. Output: {0}.".format(testOutput))

    try:
        testOutput = fibonacci(10)
        assert testOutput==55
    except AssertionError:
        print("Test fibonacci(10) failed. Output: {0}.".format(testOutput))

def floatToStringTest():
    try:
        testOutput = floatNumberToString(7.123456, -1)
        assert testOutput=="7"
    except AssertionError:
        print("Test floatNumberToString(7.123456, -1) failed. Output: {0}.".format(testOutput))

    try:
        testOutput = floatNumberToString(-7.123456)
        assert testOutput=="-7"
    except AssertionError:
        print("Test floatNumberToString(-7.123456) failed. Output: {0}.".format(testOutput))

    try:
        testOutput = floatNumberToString(7.123456, 1)
        assert testOutput=="7.1"
    except AssertionError:
        print("Test floatNumberToStr(7.123456, 1) failed. Output: {0}.".format(testOutput))

    try:
        testOutput = floatNumberToString(-7.123456, 2)
        assert testOutput=="-7.12"
    except AssertionError:
        print("Test floatNumberToString(-7.123456, 2) failed. Output: {0}.".format(testOutput))

    try:
        testOutput = floatNumberToString(7, 3)
        assert testOutput=="7"
    except AssertionError:
        print("Test floatNumberToString(7, 3) failed. Output: {0}.".format(testOutput))

    try:
        testOutput = floatNumberToString(11.0)
        assert testOutput=="11"
    except AssertionError:
        print("Test floatNumberToString(11.0) failed. Output: {0}.".format(testOutput))

    try:
        testOutput = floatNumberToString(11.0, 1)
        assert testOutput=="11.0"
    except AssertionError:
        print("Test floatNumberToString(11.0, 1) failed. Output: {0}.".format(testOutput))
    
    try:
        testOutput = floatNumberToString(11.0, 2)
        assert testOutput=="11.0"
    except AssertionError:
        print("Test floatNumberToString(11.0, 2) failed. Output: {0}.".format(testOutput))

def gcdTest():
    try:
        testOutput = greatestCommonDivisor(7.123456, 2)
    except ValueError:
        pass #Expected. Do nothing
    
    try:
        testOutput = greatestCommonDivisor(2, 7.123456)
    except ValueError:
        pass #Expected. Do nothing

    try:
        testOutput = greatestCommonDivisor(-1, 2)
        assert testOutput==1
    except AssertionError:
        print("Test greatestCommonDivisor(-1, 2) failed. Output: {0}.".format(testOutput))

    try:
        testOutput = greatestCommonDivisor(2, -1)
        assert testOutput==1
    except AssertionError:
        print("Test greatestCommonDivisor(2, -1) failed. Output: {0}.".format(testOutput))

    try:
        testOutput = greatestCommonDivisor(0, 7)
        assert testOutput==-1
    except AssertionError:
        print("Test greatestCommonDivisor(0, 7) failed. Output: {0}.".format(testOutput))

    try:
        testOutput = greatestCommonDivisor(7, 0)
        assert testOutput==-1
    except AssertionError:
        print("Test greatestCommonDivisor(7, 0) failed. Output: {0}.".format(testOutput))

    try:
        testOutput = greatestCommonDivisor(1, 8)
        assert testOutput==1
    except AssertionError:
        print("Test greatestCommonDivisor(1, 8) failed. Output: {0}.".format(testOutput))

    try:
        testOutput = greatestCommonDivisor(8, 1)
        assert testOutput==1
    except AssertionError:
        print("Test greatestCommonDivisor(8, 1) failed. Output: {0}.".format(testOutput))

    try:
        testOutput = greatestCommonDivisor(23, 19)
        assert testOutput==1
    except AssertionError:
        print("Test greatestCommonDivisor(23, 19) failed. Output: {0}.".format(testOutput))

    try:
        testOutput = greatestCommonDivisor(36, 32)
        assert testOutput==4
    except AssertionError:
        print("Test greatestCommonDivisor(36, 24) failed. Output: {0}.".format(testOutput))

def lcmTest():
    try:
        testOutput = leastCommonMultiple(-1, 3)
        assert testOutput==-1
    except AssertionError:
        print("Test leastCommonMultiple(-1, 3) failed. Output: {0}.".format(testOutput))
    
    try:
        testOutput = leastCommonMultiple(3, -1)
        assert testOutput==-1
    except AssertionError:
        print("Test leastCommonMultiple(3, -1) failed. Output: {0}.".format(testOutput))
    
    try:
        testOutput = leastCommonMultiple(0, 5)
        assert testOutput==-1
    except AssertionError:
        print("Test leastCommonMultiple(0, 5) failed. Output: {0}.".format(testOutput))
    
    try:
        testOutput = leastCommonMultiple(5, 0)
        assert testOutput==-1
    except AssertionError:
        print("Test leastCommonMultiple(5, 0) failed. Output: {0}.".format(testOutput))
    
    try:
        testOutput = leastCommonMultiple(6, 4)
        assert testOutput==12
    except AssertionError:
        print("Test leastCommonMultiple(6, 4) failed. Output: {0}.".format(testOutput))
    
def leapYearTest():
    try:
        testOutput = isLeapYear(-400)
        assert testOutput
    except AssertionError:
        print("Test isLeapYear(-400) failed. Output: {0}.".format(testOutput))

    try:
        testOutput = isLeapYear(-100)
        assert not testOutput
    except AssertionError:
        print("Test isLeapYear(-100) failed. Output: {0}.".format(testOutput))

    try:
        testOutput = isLeapYear(-4)
        assert testOutput
    except AssertionError:
        print("Test isLeapYear(-4) failed. Output: {0}.".format(testOutput))

    try:
        testOutput = isLeapYear(-1)
        assert not testOutput
    except AssertionError:
        print("Test isLeapYear(-1) failed. Output: {0}.".format(testOutput))

    try:
        testOutput = isLeapYear(0)
        assert testOutput
    except AssertionError:
        print("Test isLeapYear(0) failed. Output: {0}.".format(testOutput))
    except ValueError:
        pass #Expected exception. Do nothing.

    try:
        testOutput = isLeapYear(1)
        assert not testOutput
    except AssertionError:
        print("Test isLeapYear(1) failed. Output: {0}.".format(testOutput))

    try:
        testOutput = isLeapYear(4)
        assert testOutput
    except AssertionError:
        print("Test isLeapYear(4) failed. Output: {0}.".format(testOutput))

    try:
        testOutput = isLeapYear(100)
        assert not testOutput
    except AssertionError:
        print("Test isLeapYear(100) failed. Output: {0}.".format(testOutput))

    try:
        testOutput = isLeapYear(400)
        assert testOutput
    except AssertionError:
        print("Test isLeapYear(400) failed. Output: {0}.".format(testOutput))

def testAll():
    fibonacciTest()
    floatToStringTest()
    gcdTest()
    lcmTest()
    leapYearTest()

if __name__=="__main__":
    print("The tests will begin.")
    testAll()
    print("The tests are done.")
    system("pause")
