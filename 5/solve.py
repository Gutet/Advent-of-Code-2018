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

def part1(p):
    while True:
        c = 0
        while c < len(p) - 1:
            if (checkDifference(p[c], p[c+1])):
                del p[c]
                del p[c]            
                c -= 2
            c += 1
        if c == len(p) - 1:
            break
    return p

def part2(p):
    smallestLength = 100000
    p = part1(p)
    for i in list(range(65, 91)):
        p2 = list(p)
        p2 = filter(lambda a: a not in [i, i + 32], p2)
        tempLength = len(part1(p2))
        if (tempLength < smallestLength):
            smallestLength = tempLength
    return smallestLength

def writeResponse(star, start, solution):
    timeOnly = True if len(sys.argv) > 1 and sys.argv[1] == '1' else False
    print('Part #%s' % star)
    if (not timeOnly):
        print('Solution: %s') % solution
    end = dt.datetime.now()
    print 'Execution time: %sms' % int((end - start).total_seconds() * 1000)

writeResponse(1, dt.datetime.now(), len(part1(list(polymers))))
writeResponse(2, dt.datetime.now(), part2(list(polymers)))