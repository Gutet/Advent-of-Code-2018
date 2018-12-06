#!/usr/bin/python
import re, sys
import datetime as dt
from operator import itemgetter

class point(object):
    __slots__ = ['x', 'y', 'isInfinite', 'area']
    def __init__(self, inputRow):
        m = re.search('(\d+),\s(\d+)', inputRow)
        self.x = int(m.group(1))
        self.y = int(m.group(2))
        self.isInfinite = False
        self.area = 0

global inputList
inputList = []

with open('input.txt') as file:
    line = file.readline()
    while (line):
        inputList.append(point(line))
        line = file.readline()

def getMaxXY():
    return (max(l.x for l in inputList) + 1, max(l.y for l in inputList) + 1)

def getClosestPoint(currx, curry):
    distancePoints = {}
    for index, l in enumerate(inputList):
        distancePoints[index] = (abs(currx - l.x) + abs(curry - l.y))

    minValue = min(distancePoints.values())
    if (distancePoints.values().count(minValue) > 1):
        return '.'
    
    pointToReturn = distancePoints.keys()[distancePoints.values().index(minValue)]

    start = (0, 0)
    end = getMaxXY()

    if (currx == 0 or currx == (end[0] - 1) or curry == 0 or curry == (end[1] - 1)):
        inputList[pointToReturn].isInfinite = True

    inputList[pointToReturn].area += 1
    return pointToReturn

def getTotalDistance(currx, curry):
    totalDistance = 0
    for index, l in enumerate(inputList):
        totalDistance += (abs(currx - l.x) + abs(curry - l.y))
    return totalDistance
    
def part1():
    start = (0, 0)
    end = getMaxXY()

    for x in range(end[0]):
        for y in range(end[1]):
            getClosestPoint(x, y)
    
    return max(p.area for p in [x for x in inputList if x.isInfinite == False])

def part2():
    start = (0, 0)
    end = getMaxXY()
    area = 0
    for x in range(end[0]):
        for y in range(end[1]):
            if (getTotalDistance(x, y) < 10000):
                area += 1
    return area

def writeResponse(star, start, solution):
    timeOnly = True if len(sys.argv) > 1 and sys.argv[1] == '1' else False
    print('Part #%s' % star)
    if (not timeOnly):
        print('Solution: %s') % solution
    end = dt.datetime.now()
    print 'Execution time: %sms' % int((end - start).total_seconds() * 1000)

writeResponse(1, dt.datetime.now(), part1())
writeResponse(2, dt.datetime.now(), part2())