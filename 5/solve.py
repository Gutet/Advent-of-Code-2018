#!/usr/bin/python
import re, sys
import datetime as dt

with open('input.txt') as file:
    polymers = file.read()
polymers = [ord(x) for x in list(polymers)]

def checkDifference(a, b):
    if (abs(a-b) == 32):
        return True
    return False

def part1():
    while True:
        c = 0
        while c < len(polymers) - 1:
            if (checkDifference(polymers[c], polymers[c+1])):
                del polymers[c]
                del polymers[c]            
                c -= 2
            c += 1
        if c == len(polymers) - 1:
            break
    return len(polymers)

def part2():
    smallestLength = 100000
    for i in list(range(65, 91)):
        polymers2 = list(polymers)
        polymers2 = filter(lambda a: a not in [i, i + 32], polymers2)
        while True:
            c = 0
            while c < len(polymers2) - 1:
                if (checkDifference(polymers2[c], polymers2[c+1])):
                    del polymers2[c]
                    del polymers2[c]            
                    c -= 2
                c += 1
            if c == len(polymers2) - 1:
                break
        if (len(polymers2) < smallestLength):
            smallestLength = len(polymers2)
    return smallestLength

def writeResponse(star, start, solution):
    timeOnly = True if len(sys.argv) > 1 and sys.argv[1] == '1' else False
    print('Part #%s' % star)
    if (not timeOnly):
        print('Solution: %s') % solution
    end = dt.datetime.now()
    print 'Execution time: %sms' % int((end - start).total_seconds() * 1000)

writeResponse(1, dt.datetime.now(), part1())
writeResponse(2, dt.datetime.now(), part2())