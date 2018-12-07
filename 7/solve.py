#!/usr/bin/python
import re, sys
import datetime as dt

global assemblyInstructions
assemblyInstructions = {}

with open('input.txt') as file:
    line = file.readline()
    while (line):
        m = re.search('Step\s([A-Z]).*step\s([A-Z]).*', line)
        if (m.group(1) not in assemblyInstructions):
            assemblyInstructions[m.group(1)] = list(m.group(2))
        else:
            assemblyInstructions.setdefault(m.group(1), []).append(m.group(2))
        line = file.readline()

def getStartPoint():
    parents = []
    children = []
    for itm in assemblyInstructions:
        parents.extend(itm)
        children.extend(assemblyInstructions[itm])
    return list(set(parents) - set(children))

def getNextFulfilled(a, r):
    if (r == '' or len(a) == 1):
        return a[0]
    for c in a:
        fulfilled = True
        for k, v in assemblyInstructions.iteritems():
            if (c in v and k not in r):
                fulfilled = False
                break
        if (fulfilled):
            return str(c)

def part1():
    available = getStartPoint()
    resultString = ''
    while available is not '':
        available = ''.join(sorted(available))
        current = getNextFulfilled(available, resultString)
        resultString += current
        available = available.replace(current, '')

        if current in assemblyInstructions.keys():
            for c in assemblyInstructions[current]:
                if c not in resultString and c not in available:
                    available += c
    return resultString

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