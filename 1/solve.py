#!/usr/bin/python
import re, sys
import datetime as dt

with open('input.txt') as file:
    frequences = file.readlines()

def part1(f):
    sum = 0
    for c in f:
        sum += int(c)
    return sum

def part2(f):
    v = 0
    sum = 0
    sum_dict = {}
    sum_dict[0] = 1
    while True:
        for c in f:
            sum += int(c)
            if sum in sum_dict:
                return sum
            sum_dict[sum] = 1

frequences = map(lambda x: int(x.replace('\n', '')), frequences)

def writeResponse(star, start, solution):
    timeOnly = True if len(sys.argv) > 1 and sys.argv[1] == '1' else False
    print('Part #%s' % star)
    if (not timeOnly):
        print('Solution: %s') % solution
    end = dt.datetime.now()
    print 'Execution time: %sms' % int((end - start).total_seconds() * 1000)

writeResponse(1, dt.datetime.now(), part1(frequences))
writeResponse(2, dt.datetime.now(), part2(frequences))