#!/usr/bin/python
import re, sys
import datetime as dt
from collections import Counter

with open('input.txt') as file:
    boxes = file.readlines()
boxes = map(lambda x: (x.replace('\n', '')), boxes)

def match(s1, s2):
    pos = -1
    for i, (c1, c2) in enumerate(zip(s1, s2)):
        if c1 != c2:
            if pos != -1:
                return -1
            else:
                pos = i
    return pos

def part1():
    check_2 = 0
    check_3 = 0
    for l in boxes:
        counted = Counter(l)
        if (2 in counted.viewvalues()):
            check_2 += 1
        if (3 in counted.viewvalues()):
            check_3 += 1
    return check_2 * check_3

def part2():
    i = 0
    while i < len(boxes):
        j = i + 1
        while j < len(boxes):
            m = match(boxes[i], boxes[j])
            if (m > -1):
                return(boxes[i][:m] + boxes[i][m + 1:])
            j += 1
        i += 1

def writeResponse(star, start, solution):
    timeOnly = True if len(sys.argv) > 1 and sys.argv[1] == '1' else False
    print('Part #%s' % star)
    if (not timeOnly):
        print('Solution: %s') % solution
    end = dt.datetime.now()
    print 'Execution time: %sms' % int((end - start).total_seconds() * 1000)

writeResponse(1, dt.datetime.now(), part1())
writeResponse(2, dt.datetime.now(), part2())