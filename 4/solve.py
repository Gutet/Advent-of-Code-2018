#!/usr/bin/python
import re, sys
import datetime as dt
from operator import attrgetter
from collections import Counter

with open('input.txt') as file:
    log = file.readlines()
log = map(lambda x: (x.replace('\n', '')), log)

class logObject(object):
    __slots__ = ['time', 'action']
    def __init__(self, logRow):
        m = re.search('.*\[([0-9- :]+)\]\s(.+)*', logRow)
        self.time = m.group(1)
        self.action = m.group(2)

#Read logs and sort them
global logRecords
logRecords = []
for l in log:
    logRecords.append(logObject(l))
logRecords = sorted(logRecords, key=attrgetter('time'))

global guardPattern
guardPattern = {}

def part1():
    for l in logRecords:
        if ('Guard' in l.action):
            guardId = re.search('Guard\s#(\d+).*', l.action).group(1)
            if (guardId not in guardPattern):
                guardPattern[guardId] = []
        elif ('asleep' in l.action):
            startMinute = int(l.time[-2:])
        else:
            endMinute = int(l.time[-2:])
            guardPattern.setdefault(guardId, []).extend(list(range(startMinute, endMinute)))
    
    # Find the answer
    mostSleepy = max(guardPattern, key=lambda x: len(guardPattern[x]))
    mostMinute = Counter(guardPattern[mostSleepy]).most_common()[0][0]
    return int(mostSleepy) * int(mostMinute)

def part2():
    maxMinute, maxCount, guardId = 0, 0, 0
    for key, value in guardPattern.iteritems():
        temp = Counter(value).most_common()
        if len(temp) > 0:
            (minute, count) = temp[0]
            if (count > maxCount):
                maxCount, maxMinute, guardId = count, minute, key

    return int(maxMinute) * int(guardId)

def writeResponse(star, start, solution):
    timeOnly = True if len(sys.argv) > 1 and sys.argv[1] == '1' else False
    print('Part #%s' % star)
    if (not timeOnly):
        print('Solution: %s') % solution
    end = dt.datetime.now()
    print 'Execution time: %sms' % int((end - start).total_seconds() * 1000)

writeResponse(1, dt.datetime.now(), part1())
writeResponse(2, dt.datetime.now(), part2())