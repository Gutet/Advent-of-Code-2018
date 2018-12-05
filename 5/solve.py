#!/usr/bin/python
import re, sys
import datetime as dt

with open('input.txt') as file:
    polymers = file.read()

def part1(p):
    i = 0
    ret = ''
    while i < len(p) - 1:
        if (abs(ord(p[i]) - ord(p[i + 1])) == 32):
            i += 2
        elif (len(ret) > 0 and abs(ord(p[i]) - ord(ret[-1])) == 32):
            i += 1
            ret = ret[:-1]
        else:
            ret += p[i]
            i += 1
    return ret + p[-1]

def part2(p):
    smallestLength = 100000
    p = part1(p)
    for i in list(range(65, 91)):
        p2 = p
        p2 = p2.replace(chr(i), "").replace(chr(i + 32), "")
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

writeResponse(1, dt.datetime.now(), len(part1(polymers)))
writeResponse(2, dt.datetime.now(), part2(polymers))