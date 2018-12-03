import datetime as dt
from collections import Counter

with open('input.txt') as file:
    boxes = file.readlines()
boxes = map(lambda x: (x.replace('\n', '')), boxes)

def match(s1, s2):
    pos = -1
    for i, (c1, c2) in enumerate(zip(s1, s2)):
        if c1 != c2:
            if pos != -1:
                return -1
            else:
                pos = i
    return pos

def part1():
    check_2 = 0
    check_3 = 0
    for l in boxes:
        counted = Counter(l)
        if (2 in counted.viewvalues()):
            check_2 += 1
        if (3 in counted.viewvalues()):
            check_3 += 1
    return check_2 * check_3

def part2():
    i = 0
    while i < len(boxes):
        j = i + 1
        while j < len(boxes):
            m = match(boxes[i], boxes[j])
            if (m > -1):
                return(boxes[i][:m] + boxes[i][m + 1:])
            j += 1
        i += 1

start = dt.datetime.now()
print('Part #1: %s') % part1()
end = dt.datetime.now()
print 'Execution time: %sms' % int((end - start).total_seconds() * 1000)

start = dt.datetime.now()
print('Part #2: %s') % part2()
end = dt.datetime.now()
print 'Execution time: %sms' % int((end - start).total_seconds() * 1000)