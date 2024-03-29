def unique(iterable):
    tmp = set()
    for i in iterable:
        if i in tmp:
            continue
        else:
            tmp.add(i)
            yield i
# INPUT DATA:

# TEST_1:
numbers = [1, 2, 2, 3, 4, 5, 5, 5]

print(*unique(numbers))

# TEST_2:
iterator = iter('111222333')
uniques = unique(iterator)

print(next(uniques))
print(next(uniques))
print(next(uniques))

# TEST_3:
data = map(abs, range(-100, 100))

print(*unique(data))

# TEST_4:
data = map(str.upper, 'jhfjgshgkjfdjsgriyteryowpqerkelfsldfmnmnbmvcnmlgqweootiyoeytkldjhmvxcmkasd')

print(*unique(data))

# TEST_5:
data = 'JSKFJSDIFjejfkdjKJFIOJfkgkSDJGIEJGsklGDnvmmcvlwoqeriwjndSKF'

print(*unique(data))

# TEST_6:
data = map(str.lower, 'STEPIK')

print(*unique(data))

# TEST_7:
data = map(str.lower, 'SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS')

print(*unique(data))

# TEST_8:
data = ['bee', 'geek', 'stepik', 'python']

print(*unique(data))

# TEST_9:
print(list(unique([])))
