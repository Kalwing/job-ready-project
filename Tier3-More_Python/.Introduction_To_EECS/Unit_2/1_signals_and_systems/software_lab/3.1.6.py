"""
I will not use the library so it might not work exactly as intended
"""
import sys
sys.path.append('../../../')
from lib import SM, PureFonction, Feedback, Cascade, Delay

negate = PureFonction(lambda b: not b)
alternating = Feedback(Cascade(Delay(False), negate))

print(alternating.transduce([1,2,3,4,5,6,7]))
