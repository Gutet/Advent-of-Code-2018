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
    'borr',
    'bori',
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

def doOperation(op, reg, A, B, C):
    if (op == 'addr'):
        reg[C] = reg[A] + reg[B]
    elif (op == 'addi'):
        reg[C] = reg[A] + B
    elif (op == 'mulr'):
        reg[C] = reg[A] * reg[B]
    elif (op == 'muli'):
        reg[C] = reg[A] * B
    elif (op == 'banr'):
        reg[C] = reg[A] & reg[B]
    elif (op == 'bani'):
        reg[C] = reg[A] & B
    elif (op == 'borr'):
        reg[C] = reg[A] | reg[B]
    elif (op == 'bori'):
        reg[C] = reg[A] | B
    elif (op == 'setr'):
        reg[C] = reg[A]
    elif (op == 'seti'):
        reg[C] = A
    elif (op == 'gtir'):
        if (A > reg[B]):
            reg[C] = 1
        else:
            reg[C] = 0
    elif (op == 'gtri'):
        if (reg[A] > B):
            reg[C] = 1
        else:
            reg[C] = 0
    elif (op == 'gtrr'):
        if (reg[A] > reg[B]):
            reg[C] = 1
        else:
            reg[C] = 0
    elif (op == 'eqir'):
        if (A == reg[B]):
            reg[C] = 1
        else:
            reg[C] = 0
    elif (op == 'eqri'):
        if (reg[A] == B):
            reg[C] = 1
        else:
            reg[C] = 0
    elif (op == 'eqrr'):
        if (reg[A] == reg[B]):
            reg[C] = 1
        else:
            reg[C] = 0
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
            tempReg = doOperation(op, currentReg, values[1], values[2], values[3])

            if (tempReg == finalReg):
                if op not in opCodes[values[0]]:
                    opCodes[values[0]].append(op)
                opCodeCount += 1

        if (opCodeCount >= 3):
            totalSamples += 1
        pos += 3
        if (pos >= len(iList)):
            break

    return totalSamples

def part2(iList):
    while (getMaxCountPerCode() > 1):
        delCode, key = getCodeToRemove()
        removeCode(delCode, key)

    # All opcodes done, handle input
    reg = [0, 0, 0, 0]
    for line in iList:
        stuff = list(map(int, line.split()))
        reg = doOperation(opCodes[stuff[0]][0], reg, stuff[1], stuff[2], stuff[3])
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