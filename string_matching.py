def kmpMatch(pattern, text):
    n = len(text)
    m = len(pattern)

    fail = computeFail(pattern)

    i = 0
    j = 0
    while (i < n):
        if (pattern[j] == text[i]):
            if (j == m - 1):
                return i - m + 1
            i += 1
            j += 1
        elif (j > 0):
            j = fail[j-1]
        else:
            i += 1
    return -1

def computeFail(pattern):
    patternLength = len(pattern)
    fail = [0 for i in range(patternLength)]
    
    j = 0
    i = 1

    while (i < patternLength):
        if (pattern[j] == pattern[i]):
            fail[i] = j + 1
            i += 1
            j += 1
        elif (j > 0):
            j = fail[j-1]
        else:
            fail[i] = 0
            i += 1
    return fail

def bmMatch(pattern, text):
    last = buildLast(pattern)
    n = len(text)
    m = len(pattern)

    i = m - 1

    if (i > n-1):
        return -1
    
    j = m - 1
    while True:
        if (pattern[j] == text[i]):
            if (j == 0):
                return i
            else:
                i -= 1
                j -= 1
        else:
            lastOcc = last[ord(text[i])]
            i = i + m - min(j, lastOcc + 1)
            j = m -1
        if (i > n - 1):
            break
    return -1

def buildLast(pattern):
    last = [-1 for i in range(128)]

    for i in range(len(pattern)):
        last[ord(pattern[i])] = i

    return last