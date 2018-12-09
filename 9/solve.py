#!/usr/bin/python
import re, sys
import datetime as dt
from collections import deque

#Real input 452 players; last marble is worth 71250 points
players = 452
lastMarble = 71250

def part1(players, lastMarble):
    currentElf = 0
    elves = {}
    currentIndex = 0
    circle = deque([0])
    for current in range(1, lastMarble + 1):
        if current % 23 == 0:
            if currentElf not in elves:
                elves[currentElf] = current
            else:
                elves[currentElf] += current
            circle.rotate(7)
            elves[currentElf] += circle.pop()
            circle.rotate(-1)
        else:
            circle.rotate(-1)
            circle.append(current)
        
        currentElf = (currentElf + 1) % players
    return max(elves.values())

def writeResponse(star, start, solution):
    timeOnly = True if len(sys.argv) > 1 and sys.argv[1] == '1' else False
    print('Part #%s' % star)
    if (not timeOnly):
        print('Solution: %s') % solution
    end = dt.datetime.now()
    print 'Execution time: %sms' % int((end - start).total_seconds() * 1000)

test = [(10, 1618, 8317), (13, 7999, 146373), (17, 1104, 2764), (21, 6111, 54718), (30, 5807, 37305)]

for i in range(len(test)):
    print('Players: %s; Last marble: %s - Should be: %s' % (test[i][0], test[i][1], test[i][2]))
    print(part1(test[i][0], test[i][1]))

writeResponse(1, dt.datetime.now(), part1(players, lastMarble))
writeResponse(2, dt.datetime.now(), part1(players, lastMarble * 100))