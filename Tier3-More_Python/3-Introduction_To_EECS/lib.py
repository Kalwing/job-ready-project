"""
Homemade replacement to the library
"""
from abc import ABC, abstractmethod

class SM(ABC):
    def start(self):
        """
        Initialize the state machine.
        """
        self.state = self.start_state

    def step(self, input):
        """
        Return an output value and update the state of the state machine
        """
        next_values = self.getNextValues(self.state, input)
        self.updateState(next_values[0])
        return(next_values[1])

    def updateState(self, new_state):
        self.state = new_state

    def transduce(self, inputs):
        self.start()
        return [self.step(input) for input in inputs]

    @abstractmethod
    def getNextValues(self, state, input):
        """
        Return a tuple as so (state, output).
        """
        pass


class Delay(SM):
    def __init__(self, v0):
        self.start_state = v0

    def getNextValues(self, state, inp):
        return (inp, state)


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
