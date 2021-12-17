def RemoveOdd(list):
    return [x for x in list if x % 2 == 0]

numbers = [3, 34, 13, 41, 56, 12, 78]

print(RemoveOdd(numbers))

