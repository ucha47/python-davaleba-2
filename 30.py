import statistics

numbers = [27, 19, 6, 30, 11, 15, 8, 27, 30, 12, 3, 14, 20, 29]

numbers_sorted = sorted(numbers)

print(statistics.mean(numbers_sorted))

print(statistics.median(numbers_sorted))

print(statistics.mode(numbers_sorted))

# This function will raise the StatisticsError when the data set is empty or
# when more than one mode is present. However, in the newer versions of Python,
# the smallest element will be considered the mode when there are multiple modes of a sequence.





