import random
import math

numbers = []
for x in range(0, 10):
    x = random.randint(25, 110)
    numbers.append(x)
print(numbers)
print(min(numbers))
