#!/usr/bin/python
import re, sys, json
import datetime as dt
from collections import defaultdict

with open('input.txt') as file:
    inputlist = file.readlines()
inputlist = map(lambda x: (x.replace('\n', '')), inputlist)

p1Input = []
p2Input = [] 
blankRow = 0

for current in range(0, len(inputlist)):
    if (inputlist[current] == ''):
        blankRow += 1
    else:
        if (blankRow > 2):
            p2Input = inputlist[current:]
            break
        p1Input.append(inputlist[current])
        blankRow = 0

global opCodes
opCodes = defaultdict(list)

global removedDuplicates
removedDuplicates = []

global operations
operations = [
    'addr',
    'addi',
    'mulr',
    'muli',
    'banr',
    'bani',
    'setr',
    'seti',
    'gtir',
    'gtri',
    'gtrr',
    'eqir',
    'eqri',
    'eqrr'
]

def setRegister(line):
    m = re.search('.*\[(.*)\]', line)
    return list(map(int, m.group(1).strip().split(',')))

def doOperation(op, reg, values):
    if (op == 'addr'):
        reg[values[2]] = reg[values[0]] + reg[values[1]]
    elif (op == 'addi'):
        reg[values[2]] = reg[values[0]] + values[1]
    elif (op == 'mulr'):
        reg[values[2]] = reg[values[0]] * reg[values[1]]
    elif (op == 'muli'):
        reg[values[2]] = reg[values[0]] * values[1]
    elif (op == 'banr'):
        reg[values[2]] = reg[values[0]] & reg[values[1]]
    elif (op == 'bani'):
        reg[values[2]] = reg[values[0]] & values[1]
    elif (op == 'borr'):
        reg[values[2]] = reg[values[0]] | reg[values[1]]
    elif (op == 'bori'):
        reg[values[2]] = reg[values[0]] | values[1]
    elif (op == 'setr'):
        reg[values[2]] = reg[values[0]]
    elif (op == 'seti'):
        reg[values[2]] = values[0]
    elif (op == 'gtir'):
        if (values[0] > reg[values[1]]):
            reg[values[2]] = 1
        else:
            reg[values[2]] = 0
    elif (op == 'gtri'):
        if (reg[values[0]] > values[1]):
            reg[values[2]] = 1
        else:
            reg[values[2]] = 0
    elif (op == 'gtrr'):
        if (reg[values[0]] > reg[values[1]]):
            reg[values[2]] = 1
        else:
            reg[values[2]] = 0
    elif (op == 'eqir'):
        if (values[0] == reg[values[1]]):
            reg[values[2]] = 1
        else:
            reg[values[2]] = 0
    elif (op == 'eqri'):
        if (reg[values[0]] == values[1]):
            reg[values[2]] = 1
        else:
            reg[values[2]] = 0
    elif (op == 'eqrr'):
        if (reg[values[0]] == reg[values[1]]):
            reg[values[2]] = 1
        else:
            reg[values[2]] = 0
    else:
        print 'Illegal operator'
        sys.exit(0)

    return reg

def getCodeToRemove():
    for k, v in opCodes.iteritems():
        # if length of values is 1
        if (len(v) == 1 and v[0] not in removedDuplicates):
            removedDuplicates.append(v[0])
            return v[0], k

def getMaxCountPerCode():
    max = 0
    for k, v in opCodes.iteritems():
        if (len(v) > max):
            max = len(v)
    return max

def removeCode(code, ignoreKey):
    for k, v in opCodes.iteritems():
        if (k != ignoreKey and code in opCodes[k] and len(opCodes[k]) > 1):
            opCodes[k].remove(code)

def part1(iList):
    pos = 0
    totalSamples = 0
    while (True):
        opCodeCount = 0
        finalReg = setRegister(iList[pos + 2])

        for op in operations:
            currentReg = setRegister(iList[pos])
            values = list(map(int, iList[pos + 1].split()))
            tempReg = doOperation(op, currentReg, values[1:])

            if (tempReg == finalReg):
                opCodes[values[0]].append(op)
                opCodeCount += 1

        if (opCodeCount >= 3):
            totalSamples += 1
        pos += 3
        if (pos >= len(iList)):
            break

    return totalSamples

def part2(iList):
    # Recalculate opCodes
    for k, v in opCodes.iteritems():
        opCodes[k] = list(set(opCodes[k]))

    while (getMaxCountPerCode() > 1):
        delCode, key = getCodeToRemove()
        removeCode(delCode, key)

    print(opCodes)

    # All opcodes done, handle input
    reg = [0, 0, 0, 0]
    for line in iList:
        stuff = list(map(int, line.split()))
        print(reg)
        print('%s: %s' % (opCodes[stuff[0]][0], stuff[1:]))
        #raw_input('Press enter to continue: ')
        reg = doOperation(opCodes[stuff[0]][0], reg, stuff[1:])
    return reg[0]

def writeResponse(star, start, solution):
    timeOnly = True if len(sys.argv) > 1 and sys.argv[1] == '1' else False
    print('Part #%s' % star)
    if (not timeOnly):
        print('Solution: %s') % solution
    end = dt.datetime.now()
    print 'Execution time: %sms' % int((end - start).total_seconds() * 1000)

writeResponse(1, dt.datetime.now(), part1(p1Input))
writeResponse(2, dt.datetime.now(), part2(p2Input))