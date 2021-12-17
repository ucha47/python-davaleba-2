sentence = 'python php pascal javascript java c++'

words = sentence.split()

sortedwords = sorted(words, key=len)

print("the longest word is: ", sortedwords[-1])


