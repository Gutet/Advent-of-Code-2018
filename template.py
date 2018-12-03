import datetime as dt

with open('test.txt') as file:
    claims = file.readlines()
claims = map(lambda x: (x.replace('\n', '')), claims)

def part1():
    return 0

def part2():
    return 0

start = dt.datetime.now()
print('Part #1: %s') % part1()
end = dt.datetime.now()
print 'Execution time: %sms' % int((end - start).total_seconds() * 1000)

start = dt.datetime.now()
print('Part #2: %s') % part2()
end = dt.datetime.now()
print 'Execution time: %sms' % int((end - start).total_seconds() * 1000)