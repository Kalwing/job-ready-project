"""
I will not use the library so it might not work exactly as intended
"""
import sys
sys.path.append('../../../')
from lib import SM, Repeat


# Part 1
# Sum machine
class SumTSM(SM):
    startState = 0

    def getNextValues(self, state, input):
        if self.done(state):
            return (state, input)
        else :
            return (state + input, state + input)

    def done(self, state):
        return state > 100

print(SumTSM().transduce([25,10,25,45,25,100,300]))

# Part 2:
# Some machine

four_times = Repeat(SumTSM(), 4)
print(four_times.transduce([25,10,25,45,25,100,40,58,96,3,4,78,20,20,75,68,98, 50,25,25,68]))

# Part 3:
# Counting machine
class CountUpTo(SM):
    startState = 0

    def getNextValues(self, state, input):
        if self.done(state):
            return (state, input)
        else :
            return (state + 1, state + 1)

    def done(self, state):
        return state >= 3

print(CountUpTo().transduce([25,10,25,45,25,100,300]))
