import math


def stdDevOfLengths(L):
    """
    L: a list of strings

    returns: float, the standard deviation of the lengths of the strings,
      or NaN if L is empty.
    """
    if L is None or len(L) == 0:
        return math.nan
    X = [len(s) for s in L]
    mean = sum(X)/len(X)
    v = 0
    for x in X:
        v += (x - mean)**2
    v = v/len(X)
    stdDev = math.sqrt(v)
    return stdDev

def varCoeff(L):
    X = L
    mean = sum(X)/len(X)
    v = 0
    for x in X:
        v += (x - mean)**2
    v = v/len(X)
    stdDev = math.sqrt(v)
    return stdDev/mean

print(stdDevOfLengths(['apples', 'oranges', 'kiwis', 'pineapples']))
print(stdDevOfLengths(['a', 'z', 'p']))
print(stdDevOfLengths([]))
print(varCoeff([1,2,3]))
print(varCoeff([11,12,13]))
print(varCoeff([10,4,12,15,20,5]))
