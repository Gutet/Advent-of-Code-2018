#!/usr/bin/python
import re, sys
import datetime as dt
from collections import defaultdict

with open('input.txt') as file:
    inputlist = file.readlines()
inputlist = map(lambda x: (x.replace('\n', '')), inputlist)

initialState = '....' + inputlist[0].replace('initial state: ','') + '....'

spread = {}
for i in range(2, len(inputlist)):
    t = inputlist[i].split(' => ')
    spread[t[0]] = t[1]

def fillWithDots(state, zeroPos):
    while (not state.endswith('....')):
        state += '.'
    while (not state.startswith('....')):
        zeroPos += 1
        state = '.' + state
    return state, zeroPos

def calculateSum(state, zeroPos):
    sum = 0
    val = -1 * zeroPos
    for i in range(len(state)):
        if (state[i] == '#'):
            sum += val
        val += 1
    return sum


def part1(state, spread):
    zeroPos = 4
    for i in range(20):
        nextState = '..'
        for c in range(2, len(state) - 2):
            rule = state[c-2:c+3]
            if (rule in spread):
                nextState += spread[rule]
            else:
                nextState += '.'
        state, zeroPos = fillWithDots(nextState, zeroPos)
    return calculateSum(state, zeroPos)

def part2(state, spread):
    zeroPos = 4
    lastSum = 0
    currentSum = 0
    for i in range(500):
        nextState = '..'
        for c in range(2, len(state) - 2):
            rule = state[c-2:c+3]
            if (rule in spread):
                nextState += spread[rule]
            else:
                nextState += '.'
        
        # No change?
        nextStrip = nextState.lstrip('.').rstrip('.')
        currStrip = state.lstrip('.').rstrip('.')

        if (nextStrip == currStrip and nextState.startswith('.....')):
            currentSum = calculateSum(nextState, zeroPos)
            lastSum = calculateSum(state, zeroPos)

            difference = currentSum - lastSum

            if ((i+1) % 100 == 0):
                sum = lastSum
                sum += (50000000000 - i) * difference
                return sum
        
        state, zeroPos = fillWithDots(nextState, zeroPos)
    return 0

def writeResponse(star, start, solution):
    timeOnly = True if len(sys.argv) > 1 and sys.argv[1] == '1' else False
    print('Part #%s' % star)
    if (not timeOnly):
        print('Solution: %s') % solution
    end = dt.datetime.now()
    print 'Execution time: %sms' % int((end - start).total_seconds() * 1000)

writeResponse(1, dt.datetime.now(), part1(initialState, spread))
writeResponse(2, dt.datetime.now(), part2(initialState, spread))
