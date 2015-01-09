import string
inputFile = open(r'Resources/TaleOfTwoCities.txt', 'r')

wordsSet = set()
wordsDict = {}

count = 0
for line in inputFile:
    words = line.split()
    words = [str.lower().strip(string.punctuation) for str in words]
    for word in words:
        count += 1
        wordsSet.add(word)
        if wordsDict.get(word) == None:
            wordsDict[word] = 1
        else:
            wordsDict[word] += 1

print('Total words in the file: %d' % (count))
print('Number of unique words in the file: %d' % (len(wordsSet)))

val = list(wordsDict.values())
keys = list(wordsDict.keys())
common = keys[val.index(max(val))]
print('The most common word in the file: %s' % (common))
print('Humility count: %d\nChapter count: %d\nWe count: %d\n' % (wordsDict['humility'], wordsDict['chapter'], wordsDict['we']))


