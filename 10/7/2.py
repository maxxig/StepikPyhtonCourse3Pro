def parse_ranges(ranges):
    for item in ranges.split(','):
        _split = item.split('-')
        for s in range(int(_split[0]),int(_split[1])+1):
            yield s

# INPUT DATA:

# TEST_1:
print(*parse_ranges('1-2,4-4,8-10'))

# TEST_2:
print(*parse_ranges('1-10,2-10'))

# TEST_3:
print(*parse_ranges('7-32'))

# TEST_4:
print(*parse_ranges('8-8,8-8,8-8,8-8,8-8'))

# TEST_5:
print(*parse_ranges('10-10,11-11,12-12'))

# TEST_6:
print(*parse_ranges('10-15,1-4,4-5,5-5,1-10,1-15'))

# TEST_7:
numbers = parse_ranges('1-3')

print(next(numbers))
print(next(numbers))
print(next(numbers))

# TEST_8:
numbers = parse_ranges('1-3,4-5,10-32,32-32,32-40,1-2,2-32,10-11,67-199')

print(*numbers)
