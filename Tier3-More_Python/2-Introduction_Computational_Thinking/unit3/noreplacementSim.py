import random


def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3
    balls of the same color were drawn.
    '''
    RED, GREEN = 1, 0
    nbSameColor = 0
    for n in range(numTrials):
        bucket = [RED, RED, RED, GREEN, GREEN, GREEN]
        out = 0
        for i in range(3):
            drawn = random.choice(bucket)
            bucket.remove(drawn)
            out += drawn
        if out in (3*RED, 3*GREEN):
            nbSameColor += 1
    return nbSameColor/numTrials

for i in range(1,5001,1000):
    print(noReplacementSimulation(i))
