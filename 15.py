import statistics

numbs = [4, 7, 16, 46, 30]
print(max(numbs))
print(min(numbs))
print(statistics.mean(numbs))
numbs.append(102)
numbs.insert(2, 205)
numbs.pop(3)
numbs.sort()
print(numbs)