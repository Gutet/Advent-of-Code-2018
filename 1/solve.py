import datetime as dt

with open('input.txt') as file:
    frequences = file.readlines()

def part1(f):
    sum = 0
    for c in f:
        sum += int(c)
    return sum

def part2(f):
    v = 0
    sum = 0
    sum_dict = {}
    sum_dict[0] = 1
    while True:
        for c in f:
            sum += int(c)
            if sum in sum_dict:
                return sum
            sum_dict[sum] = 1

frequences = map(lambda x: int(x.replace('\n', '')), frequences)

start = dt.datetime.now()
print('Part #1: %s') % part1(frequences)
end = dt.datetime.now()
print 'Execution time: %sms' % int((end - start).total_seconds() * 1000)

start = dt.datetime.now()
print('Part #2: %s') % part2(frequences)
end = dt.datetime.now()
print 'Execution time: %sms' % int((end - start).total_seconds() * 1000)