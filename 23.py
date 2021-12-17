numbers = [11, 14, 27, 39, 54, 91, 70]

def remover(x):
    new_numbers = []
    for i in x:
        if i % 2 == 0:
            new_numbers.append(i)
    return new_numbers

print(remover(numbers))