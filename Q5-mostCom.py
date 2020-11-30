# Program to find the most common
# N words using collections module

from collections import Counter

n = int(input("Enter the value of n: "))

words = ['red', 'green', 'black', 'pink', 'black', 'white', 'black', 'eyes',
'white', 'black', 'orange', 'pink', 'pink', 'red', 'red', 'white', 'orange',
'white', "black", 'pink', 'green', 'green', 'pink', 'green', 'pink',
'white', 'orange', "orange", 'red']

def getCommon(words, n):
    counts = Counter(words)
    total_count = counts.most_common()
    if n > total_count:
        return("Number of desired words exceeds the total word count!")
    return("Most common {} words are: {}".format(n, counts.most_common(n)))

print(getCommon(words, n))
