numbers1 = [3, 66, 31, 43, 17]
numbers2 = [4, 15, 56, 1, 66]

def twolists(x, y):
    for i in x:
        if i in y:
            return True
    return False


print(twolists(numbers1, numbers2))