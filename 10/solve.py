#!/usr/bin/python
import re, sys
import datetime as dt
from operator import attrgetter

class point(object):
    __slots__ = ['pos_x', 'pos_y', 'vel_x', 'vel_y']
    def __init__(self, inputRow):
        m = re.search('position=<[\s]?(.*),[\s]?(.*).*>.*<[\s]?(.*),[\s]?(.*)>', inputRow)
        self.pos_x = int(m.group(1))
        self.pos_y = int(m.group(2))
        self.vel_x = int(m.group(3))
        self.vel_y = int(m.group(4))

global inputList
inputList = []

lastWidth = 1000000
lastHeight = 1000000

with open('input.txt') as file:
    line = file.readline()
    while (line):
        inputList.append(point(line))
        line = file.readline()

def printInput():
    for x in inputList:
        print('x: %s, y: %s - v_x: %s, v_y: %s' % (x.pos_x, x.pos_y, x.vel_x, x.vel_y))

def calculateNewPos(reverse = False):
    if (reverse):
        for i in range(len(inputList)):
            inputList[i].pos_x = inputList[i].pos_x - inputList[i].vel_x
            inputList[i].pos_y = inputList[i].pos_y - inputList[i].vel_y
    else:
        for i in range(len(inputList)):
            inputList[i].pos_x = inputList[i].pos_x + inputList[i].vel_x
            inputList[i].pos_y = inputList[i].pos_y + inputList[i].vel_y

def getBoundaries():
    min_x = min(inputList, key=attrgetter('pos_x'))
    max_x = max(inputList, key=attrgetter('pos_x'))
    min_y = min(inputList, key=attrgetter('pos_y'))
    max_y = max(inputList, key=attrgetter('pos_y'))
    return min_x.pos_x, min_y.pos_y, max_x.pos_x, max_y.pos_y

def printMatrix():
    global lastWidth
    global lastHeight
    # Create matrix
    x, y, xx, yy = getBoundaries()
    width = abs(x - xx) + 1
    height = abs(y - yy) + 1

    # Need to print?
    needToPrint = (lastHeight < height or lastWidth < width)
    if (needToPrint):
        calculateNewPos(True)
        x, y, xx, yy = getBoundaries()
        
        matrix = [['.' for w in range(lastWidth)] for h in range(lastHeight)]
        # Fill matrix
        for p in inputList:
            matrix[p.pos_y - y][p.pos_x - x] = '#'
        
        # Print matrix
        for row in matrix:
            s = ''
            for elem in row:
                s += elem
            print (s)
    else:
        lastHeight = height
        lastWidth = width
    return needToPrint

def part1():
    seconds = -1
    while not printMatrix():
        seconds += 1
        calculateNewPos()        
    return seconds

def writeResponse(star, start, solution):
    timeOnly = True if len(sys.argv) > 1 and sys.argv[1] == '1' else False
    print('Part #%s' % star)
    if (not timeOnly):
        print('Solution: %s') % solution
    end = dt.datetime.now()
    print 'Execution time: %sms' % int((end - start).total_seconds() * 1000)

writeResponse('1-2', dt.datetime.now(), part1())