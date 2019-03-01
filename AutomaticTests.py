#File: AutomaticTests.py

from CustomFunctions import *
from os import system

def fibonacciTest():        
    try:
        testResult = fibonacci(-1)
    except ValueError: pass #Expected. Do nothing.
    
    try:
        assert fibonacci(0)==0
    except AssertionError: print("Test fibonacci(0) failed.")
        
    try:
        assert fibonacci(1)==1
    except AssertionError: print("Test fibonacci(1) failed.")
        
    try:
        assert fibonacci(2)==1
    except AssertionError: print("Test fibonacci(2) failed.")
        
    try:
        assert fibonacci(3)==2
    except AssertionError: print("Test fibonacci(3) failed.")
        
    try:
        assert fibonacci(10)==55
    except AssertionError: print("Test fibonacci(10) failed.")

def floatToStringTest():
    try:
        assert floatNumberToString(7.123456, -1) == "7"
    except AssertionError: print("Test floatNumberToString(7.123456, -1) failed.")
    
    try:
        assert floatNumberToString(-7.123456) == "-7"
    except AssertionError: print("Test floatNumberToString(7.123456) failed.")
    
    try:
        assert floatNumberToString(7.123456, 1) == "7.1"
    except AssertionError: print("Test floatNumberToStr(7.123456, 1) failed.")
    
    try:
        assert floatNumberToString(-7.123456, 2) == "-7.12"
    except AssertionError: print("Test floatNumberToString(7.123456, 2) failed.")
    
    try:
        assert floatNumberToString(7, 3) == "7"
    except AssertionError: print("Test floatNumberToString(7, 3) failed.")
    
    try:
        assert floatNumberToString(11.0) == "11"
    except AssertionError: print("Test floatNumberToString(11) failed.")
    
    try:
        assert floatNumberToString(11.0, 1) == "11.0"
    except AssertionError: print("Test floatNumberToString(11, 1) failed.")
    
    try:
        assert floatNumberToString(11.0, 2) == "11.0"
    except AssertionError: print("Test floatNumberToString(11, 2) failed.")

def gcdTest():
    try:
        assert greatestCommonDivider(-1, 2)==-1
    except AssertionError: print("Test greatestCommonDivider(-1, 2) failed.")

    try:
        assert greatestCommonDivider(2, -1)==-1
    except AssertionError: print("Test greatestCommonDivider(2, -1) failed.")

    try:
        assert greatestCommonDivider(0, 7)==-1
    except AssertionError: print("Test greatestCommonDivider(0, 7) failed.")

    try:
        assert greatestCommonDivider(7, 0)==-1
    except AssertionError: print("Test greatestCommonDivider(7, 0) failed.")

    try:
        assert greatestCommonDivider(1, 8)==1
    except AssertionError: print("Test greatestCommonDivider(1, 8) failed.")

    try:
        assert greatestCommonDivider(8, 1)==1
    except AssertionError: print("Test greatestCommonDivider(8, 1) failed.")

    try:
        assert greatestCommonDivider(23, 19)==1
    except AssertionError: print("Test greatestCommonDivider(23, 19) failed.")

    try:
        assert greatestCommonDivider(36, 32)==4
    except AssertionError: print("Test greatestCommonDivider(36, 24) failed.")

def lcmTest():
    try:
        assert leastCommonMultiple(-1, 3)==-1
    except AssertionError: print("Test leastCommonMultiple(-1, 3) failed.")
    
    try:
        assert leastCommonMultiple(3, -1)==-1
    except AssertionError: print("Test leastCommonMultiple(3, -1) failed.")
    
    try:
        assert leastCommonMultiple(0, 5)==-1
    except AssertionError: print("Test leastCommonMultiple(0, 5) failed.")
    
    try:
        assert leastCommonMultiple(5, 0)==-1
    except AssertionError: print("Test leastCommonMultiple(5, 0) failed.")
    
    try:
        assert leastCommonMultiple(6, 4)==12
    except AssertionError: print("Test leastCommonMultiple(6, 4) failed.")
    
def leapYearTest():
    try:
        assert isLeapYear(-400)
    except AssertionError: print("Test isLeapYear(-400) failed.")
    
    try:
        assert not isLeapYear(-100)
    except AssertionError: print("Test isLeapYear(-100) failed.")
    
    try:
        assert isLeapYear(-4)
    except AssertionError: print("Test isLeapYear(-4) failed.")
    
    try:
        assert not isLeapYear(-1)
    except AssertionError: print("Test isLeapYear(-1) failed.")
    
    try:
        assert isLeapYear(0)
    except AssertionError: print("Test isLeapYear(0) failed.")
    except ValueError: pass #Expected exception. Do nothing.
    
    try:
        assert not isLeapYear(1)
    except AssertionError: print("Test isLeapYear(1) failed.")
    
    try:
        assert isLeapYear(4)
    except AssertionError: print("Test isLeapYear(4) failed.")
    
    try:
        assert not isLeapYear(100)
    except AssertionError: print("Test isLeapYear(100) failed.")
    
    try:
        assert isLeapYear(400)
    except AssertionError: print("Test isLeapYear(400) failed.")

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
