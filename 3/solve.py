import datetime as dt

with open('input.txt') as file:
    claims = file.readlines()
claims = map(lambda x: (x.replace('\n', '')), claims)

class Claim():
    def __init__(self, line):
        line = line.split(' ')
        self.id = int(line[0][1:])
        self.x = int(line[2].replace(':','').split(',')[0])
        self.y = int(line[2].replace(':','').split(',')[1])
        self.width = int(line[3].split('x')[0])
        self.height = int(line[3].split('x')[1])
        self.overlaps = False

nodes = {}

def part1():
    for l in claims:
        c = Claim(l)
        x = c.x
        while x < (c.x + c.width):
            y = c.y
            while y < (c.y + c.height):
                pos = 'x%sy%s' % (x, y)
                if pos in nodes:
                    nodes[pos] += 1
                else:
                    nodes[pos] = 1
                y += 1
            x += 1
    overlapping = 0
    for k, v in nodes.iteritems():
        if (v > 1):
            overlapping += 1
    return overlapping

def part2():
    global nodes
    for l in claims:
        c = Claim(l)
        x = c.x
        while x < (c.x + c.width):
            y = c.y
            while y < (c.y + c.height):
                pos = 'x%sy%s' % (x, y)
                if pos in nodes and nodes[pos] > 1:
                    c.overlaps = True
                y += 1
            x += 1
        if (c.overlaps == False):
            return c.id

    return 0

start = dt.datetime.now()
print('Part #1: %s') % part1()
end = dt.datetime.now()
print 'Execution time: %sms' % int((end - start).total_seconds() * 1000)

start = dt.datetime.now()
print('Part #2: %s') % part2()
end = dt.datetime.now()
print 'Execution time: %sms' % int((end - start).total_seconds() * 1000)