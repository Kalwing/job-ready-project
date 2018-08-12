"""
I will not use the library so it might not work exactly as intended
"""
import sys
sys.path.append('../../')
from lib import SM


class Cascade(SM):
    def __init__(self, sm1, sm2):
        self.m1 = sm1
        self.m2 = sm2
        self.start_state = (self.m1.start_state, self.m2.start_state)

    def getNextValues(self, state, input):
        """
        Return a tuple as so (state, output).
        """
        m1_next_values = self.m1.getNextValues(state[0], input)
        m2_next_values = self.m2.getNextValues(state[1],
                                               m1_next_values[1])
        return ((m1m1_next_values[0], m2m2_next_values[0]),
                m2m2_next_values[1])
