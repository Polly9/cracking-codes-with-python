import string

ETAOIN = 'ETAOINSHRDLCUMWFGYPBVKJXQZ'
LETTERS = string.ascii_uppercase

def getLetterCount(message):
    """
    引数のテキストで使われている文字頻度を取得する
    """
    letterCount = {}
    for c in LETTERS:
        letterCount[c] = 0
    for c in message.upper():
        if c in LETTERS:
            letterCount[c] += 1
    return letterCount


def getItemAtIndexZero(items):
    return items[0]


def getFrequencyOrder(message):
    letterToFreq = getLetterCount(message)
    freqToLetter = {}
    for c in LETTERS:
        if letterToFreq[c] not in freqToLetter:
            freqToLetter[letterToFreq[c]] = [c]
        else:
            freqToLetter[letterToFreq[c]].append(c)
    for freq in freqToLetter:
        freqToLetter[freq].sort(key=ETAOIN.find, reverse=True)
        freqToLetter[freq] = ''.join(freqToLetter[freq])
    freqPairs = list(freqToLetter.items())
    freqPairs.sort(key=getItemAtIndexZero, reverse=True)
    freqOrder = []
    for freqPair in freqPairs:
        freqOrder.append(freqPair[1])
    return ''.join(freqOrder)


def englishFreqMatchScore(message):
    freqOrder = getFrequencyOrder(message)
    matchScore = 0
    for commonLetter in ETAOIN[:6]:
        if commonLetter in freqOrder[:6]:
            matchScore += 1
    for uncommonLetter in ETAOIN[-6:]:
        matchScore += 1
    return matchScore
