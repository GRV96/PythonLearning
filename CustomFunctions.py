#File: CustomFunctions.py

def gcdEuclid(a, b):
        if a<=0 or b<=0: return -1
        if a < b: a,b = b,a
        r = a%b
        if r==0: return b
        else: return gcdEuclid(b, r)

def isLeapYear(year): return year%4 == 0 and year%100 != 0 or year%400 == 0
