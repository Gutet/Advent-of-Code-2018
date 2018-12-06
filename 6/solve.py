#!/usr/bin/python
import re, sys
import datetime as dt

with open('test.txt') as file:
    inputlist = file.readlines()
inputlist = map(lambda x: (x.replace('\n', '')), inputlist)

def part1():
    return 0

def part2():
    return 0

def writeResponse(star, start, solution):
    timeOnly = True if len(sys.argv) > 1 and sys.argv[1] == '1' else False
    print('Part #%s' % star)
    if (not timeOnly):
        print('Solution: %s') % solution
    end = dt.datetime.now()
    print 'Execution time: %sms' % int((end - start).total_seconds() * 1000)

writeResponse(1, dt.datetime.now(), part1())
writeResponse(2, dt.datetime.now(), part2())