#!/usr/bin/python
import re, sys
import datetime as dt

def getPowerLevel(x, y, serial):
    rackId = x + 10
    powerLevel = rackId * y
    powerLevel += serial
    powerLevel *= rackId
    powerLevel = (powerLevel % 1000 - powerLevel % 100) / 100
    return powerLevel - 5

def getMatrix(serial):
    matrix = [['' for w in range(300)] for h in range(300)]
 
    for y in range(300):
        for x in range(300):
            matrix[y][x] = getPowerLevel(x + 1, y + 1, serial)
    return matrix

def getSum(matrix, xx, yy, size):
    sum = 0
    for y in range(yy, yy + size):
        for x in range(xx, xx + size):
            sum += matrix[y][x]
    return sum

def part1(serial):
    matrix = getMatrix(serial)
    maxSum = 0
    maxPos = (0, 0)
    for y in range(298):
        for x in range(298):
            sum = getSum(matrix, x, y, 3)
            if sum > maxSum:
                maxSum = sum
                maxPos = (x, y)
    return ('MaxSum: %s @ %s,%s' % (maxSum, maxPos[0] + 1, maxPos[1] + 1))

def part2(serial):
    matrix = getMatrix(serial)
    maxSum = 0
    maxPosAndSize = (0, 0, 0)
    sumDecreasesCount = 0
    lastSum = -10000
    for y in range(300):
        for x in range(300):
            sumDecreasesCount = 0
            # For each possible size...
            maxSize = min(300 - x, 300 - y)
            for size in range(maxSize):
                sum = getSum(matrix, x, y, size)
                if (sum < lastSum):
                    sumDecreasesCount += 1
                else:
                    sumDecreasesCount = 0
                # If sum has decreased 4 times in a row, break
                if (sumDecreasesCount > 4):
                    break
                lastSum = sum
                if sum > maxSum:
                    maxSum = sum
                    maxPosAndSize = (x, y, size)
    return ('MaxSum: %s @ %s,%s - with Size: %s' % (maxSum, maxPosAndSize[0] + 1, maxPosAndSize[1] + 1, maxPosAndSize[2]))

def writeResponse(star, start, solution):
    timeOnly = True if len(sys.argv) > 1 and sys.argv[1] == '1' else False
    print('Part #%s' % star)
    if (not timeOnly):
        print('Solution: %s') % solution
    end = dt.datetime.now()
    print 'Execution time: %sms' % int((end - start).total_seconds() * 1000)

writeResponse(1, dt.datetime.now(), part1(3031))
writeResponse(2, dt.datetime.now(), part2(3031))