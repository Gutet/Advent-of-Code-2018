#!/usr/bin/python
import re, sys
import datetime as dt

with open('input.txt') as file:
    inputlist = file.readlines()
inputlist = map(lambda x: (x.replace('\n', '')), inputlist)

class Instruction(object):
    __slots__ = ['operation', 'a', 'b', 'c']
    def __init__(self, row):
        l = row.split(' ')
        self.operation = l[0]
        self.a = int(l[1])
        self.b = int(l[2])
        self.c = int(l[3])

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

def part1(input):
    ins = []
    pointer = int(input[0].replace('#ip ', ''))
    for x in range(1, len(input)):
        ins.append(Instruction(input[x]))
    reg = [0, 0, 0, 0, 0, 0]

    while (reg[pointer] >= 0 and reg[pointer] < len(ins)):
        reg = doOperation(ins[reg[pointer]].operation, reg, ins[reg[pointer]].a, ins[reg[pointer]].b, ins[reg[pointer]].c)
        reg[pointer] += 1
    return reg[0]

def part2_manual(input):
    ins = []
    pointer = int(input[0].replace('#ip ', ''))
    for x in range(1, len(input)):
        ins.append(Instruction(input[x]))
    reg = [1, 0, 0, 0, 0, 0]

    while (reg[pointer] >= 0 and reg[pointer] < len(ins)):
        print(reg)
        print('%d: %s - %d %d %d' % (reg[pointer], ins[reg[pointer]].operation, ins[reg[pointer]].a, ins[reg[pointer]].b, ins[reg[pointer]].c))

        #if (ins[reg[pointer]].operation.startswith('eq') or ins[reg[pointer]].operation.startswith('gt')):
        num = raw_input('Press enter to continue: ')
        if (len(num) > 0):
            l = num.split(' ')
            reg[int(l[0])] = int(l[1])

        reg = doOperation(ins[reg[pointer]].operation, reg, ins[reg[pointer]].a, ins[reg[pointer]].b, ins[reg[pointer]].c)
        reg[pointer] += 1
        
    return reg[0]

def part2(value):
    r0 = sum([x for x in range(1, value+1) if value % x == 0])
    return r0

def writeResponse(star, start, solution):
    timeOnly = True if len(sys.argv) > 1 and sys.argv[1] == '1' else False
    print('Part #%s' % star)
    if (not timeOnly):
        print('Solution: %s') % solution
    end = dt.datetime.now()
    print 'Execution time: %sms' % int((end - start).total_seconds() * 1000)

writeResponse(1, dt.datetime.now(), part1(inputlist))
writeResponse(2, dt.datetime.now(), part2(10551396))
