#File: CustomFunctions.py

def fibonacci(n):
        if n<0: raise ValueError("The Fibonacci sequence is only defined for n>=0.")
        elif n==0: return 0
        elif n==1: return 1
        f0 = 0
        f1 = 1
        i = 1
        while i<n:
                fSum = f1 + f0
                f0 = f1
                f1 = fSum
                i += 1
        return f1

def floatNumberToString(floatN, precision=0):
        #if precision<0: precision = 0
        numberStr = str(floatN)
        pointIndex = numberStr.find('.')
        if pointIndex<0: return numberStr
        if precision<=0: return numberStr[0: pointIndex]
        else: return numberStr[0: pointIndex+precision+1]

def greatestCommonDivider(a, b):
        #Euclidian algorithm
        if a<=0 or b<=0: return -1
        if a < b: a,b = b,a
        r = a%b
        if r==0: return b
        else: return greatestCommonDivider(b, r)

def isLeapYear(year):
        if year==0: raise ValueError("Year 0 does not exist.")
        return year%4==0 and year%100!=0 or year%400==0

def leastCommonMultiple(a, b):
        if a<=0 or b<=0: return -1
        else: return int(a*b/greatestCommonDivider(a, b))
