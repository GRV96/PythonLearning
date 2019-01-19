#File: CustomFunctions.py

def greatestCommonDivider(a, b):
        #Euclidian algorithm
        if a<=0 or b<=0: return -1
        if a < b: a,b = b,a
        r = a%b
        if r==0: return b
        else: return greatestCommonDivider(b, r)

def isLeapYear(year): return year%4 == 0 and year%100 != 0 or year%400 == 0

def leastCommonMultiple(a, b):
        if a<=0 or b<=0: return -1
        else: return int(a*b/greatestCommonDivider(a, b))
