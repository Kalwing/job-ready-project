"""
I will not use the library so it might not work exactly as intended
"""
import sys
sys.path.append('../../../')
from lib import SM, PureFonction, Cascade, Parallel, Parallel2

class BA1(SM):
    startState = 0
    def getNextValues(self, state, inp):
        if inp != 0:
            newState = state * 1.02 + inp - 100
        else:
            newState = state * 1.02
        return (newState, newState)


class BA2(SM):
    startState = 0
    def getNextValues(self, state, inp):
        newState = state * 1.01 + inp
        return (newState, newState)

# Part 1: Maximize

# Make a state machine that computes the balances of both types of accounts, but
# whose output is the maximum of the two balances.
maxAccount = Cascade(Parallel(BA1(), BA2()),
                     PureFonction(lambda a: a[0] if a[0] > a[1] else a[1]))

print(maxAccount.transduce([+105,0,0,0,0,0,0]))

# Part 2: Investment
#
# My business has two bank accounts, as above. I put any deposit or withdrawal
# whose magnitude is greater than $3,000 in the account of type 1, and
# all other deposits and withdrawals in the account of type 2. On every step,
# both accounts should continue to earn the relevant interest. The output
# should be the sum of the balances in the two accounts.
switchMore3000 = PureFonction(lambda a: (a, 0) if a > 3000 else (0, a))
switchAccount = Cascade(Cascade(switchMore3000,
                                Parallel2(BA1(), BA2())),
                        PureFonction(lambda a: a[0] + a[1]))

print(switchAccount.transduce([+105,+2, +3,+40,+3528,-100]))
