"""
I will not use the library so it might not work exactly as intended
"""
import sys
sys.path.append('../../')
from lib import SM


class PureFonction(SM)
    def __init__(self, f):
        self.function = f
        self.start_state = None

    def getNextValues(self, state, input):
        return (state, self.function(input))
