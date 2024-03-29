def first_largest(iterable, number):
    res_index = -1
    for index, item in enumerate(iterable):
        if item > number:
            res_index = index
            break
    return  res_index


# TEST_4:
iterator = iter([18, 21, 14, 72, 73, 18, 20, 101, 102, 110])

print(first_largest(iterator, 105))

# TEST_5:
iterator = iter([123, 423, 224, 722, 713, 158, 230, 1101, 1022, 1210, 222, 333, 334])

print(first_largest(iterator, 105))

# TEST_6:
iterator = iter([2, 3, 4, 5, 6, 7, 8, 999])

print(first_largest(iterator, 105))

# TEST_7:
iterator = iter([999])

print(first_largest(iterator, 105))

# TEST_8:
iterator = iter([998])

print(first_largest(iterator, 999))

# TEST_9:
iterator = iter([4, 100, 102, 334, 5])

print(first_largest(iterator, 101))

# TEST_10:
print(first_largest([], 7))

# TEST_11:
iterator = iter([-400, -100, -102, -334, -5])

print(first_largest(iterator, -6))