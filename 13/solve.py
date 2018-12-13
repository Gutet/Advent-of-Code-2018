#!/usr/bin/python
import re, sys
import datetime as dt
from collections import deque
import operator
import time
import copy

with open('input.txt') as file:
    inputlist = file.readlines()
inputlist = map(lambda x: (x.replace('\n', '')), inputlist)

data = [[c for c in list(line)] for line in inputlist]

class Cart(object):
    __slots__ = ['x', 'y', 'direction', 'turn', 'delete']
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction
        self.turn = deque(['<', '^', '>'])
        self.delete = False

global turnDict
turnDict = { '^/': '>', '^\\': '<', 'v/': '<', 'v\\': '>', '>/': '^', '>\\': 'v', '</': 'v', '<\\': '^' }
global inteDict
inteDict =  { '<<': 'v', '<>': '^', '><': '^', '>>': 'v', '^<': '<', '^>': '>', 'v<': '>', 'v>': '<', '<^': '<', '>^': '>', '^^': '^', 'v^': 'v'}

def printGrid(data, carts):
    green = '\033[92m'
    nc = '\033[0m'
    for y in range(len(data)):
        s = ''
        for x in range(len(data[y])):
            hasCart = False
            for c in carts:
                if c.x == x and c.y == y:
                    hasCart = True
                    s += '%s%s%s' % (green, c.direction, nc)
                    break
            if not hasCart:
                s += data[y][x]
        print(s)

def getCarts(data):
    directions = ['<', '>', '^', 'v']
    carts = []
    for y in range(len(data)):
        for x in range(len(data[y])):
            if data[y][x] in directions:
                carts.append(Cart(x, y, data[y][x]))
    return carts

def removeCartsFromGrid(data, carts):
    for cart in carts:
        if (cart.direction in ['<', '>']):
            data[cart.y][cart.x] = '-'
        else:
            data[cart.y][cart.x] = '|'
    return data

def getCollision(data, carts, firstOnly = True):
    for i1 in range(len(carts)):
        for i2 in range(i1 + 1, len(carts)):
            if carts[i1].x == carts[i2].x and carts[i1].y == carts[i2].y:
                carts[i1].delete = True
                carts[i2].delete = True
                if firstOnly:
                    return True, carts[i1].x, carts[i1].y
    return False, 0, 0

def moveCart(data, c):
    if c.direction == '>':
        c.x += 1
    elif c.direction == '<':
        c.x -= 1
    elif c.direction == 'v':
        c.y += 1
    else:
        c.y -= 1
    
    # Bend or Intersection?
    if data[c.y][c.x] in ['/', '\\']:
        turnKey = '%s%s' % (c.direction, data[c.y][c.x])
        c.direction = turnDict[turnKey]
    elif data[c.y][c.x] == '+':
        turnKey = '%s%s' % (c.direction, c.turn[0])
        c.direction = inteDict[turnKey]
        c.turn.rotate(-1)   
    
    return c

def part1(d):
    data = copy.deepcopy(d)
    carts = getCarts(data)
    data = removeCartsFromGrid(list(data), carts)
    collision = False
    while not collision:
        carts.sort(key=lambda x: (x.y,x.x), reverse=False)
        for c in carts:
                c = moveCart(data, c)
                collision, cx, cy = getCollision(data, carts, True)
                if (collision):
                    return '%d,%d' % (cx, cy)
        #printGrid(data, carts)
        #raw_input('Press enter to continue: ')
    return 0

def part2(data):
    carts = getCarts(data)
    data = removeCartsFromGrid(data, carts)
    collision = False
    while len(carts) > 1:
        carts.sort(key=lambda x: (x.y,x.x), reverse=False)
        for i in range(len(carts)):
            carts[i] = moveCart(data, carts[i])
            collision, cx, cy = getCollision(data, carts, False)
        carts = [item for item in carts if item.delete == False]
        #printGrid(data, carts)
        #raw_input('Press enter to continue: ')
    return '%s,%s' % (carts[0].x, carts[0].y)

def writeResponse(star, start, solution):
    timeOnly = True if len(sys.argv) > 1 and sys.argv[1] == '1' else False
    print('Part #%s' % star)
    if (not timeOnly):
        print('Solution: %s') % solution
    end = dt.datetime.now()
    print 'Execution time: %sms' % int((end - start).total_seconds() * 1000)

writeResponse(1, dt.datetime.now(), part1(data))
writeResponse(2, dt.datetime.now(), part2(data))