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
        return ((m1_next_values[0], m2_next_values[0]),
                m2_next_values[1])


class PureFonction(SM):
    def __init__(self, f):
        self.function = f
        self.start_state = None

    def getNextValues(self, state, input):
        return (state, self.function(input))


class Parallel(SM):
    def __init__(self, sm1, sm2):
        self.m1 = sm1
        self.m2 = sm2
        self.start_state = (sm1.start_state, sm2.start_state)

    def getNextValues(self, state, inp):
        (s1, s2) = state
        (newS1, o1) = self.m1.getNextValues(s1, inp)
        (newS2, o2) = self.m2.getNextValues(s2, inp)
        return ((newS1, newS2), (o1, o2))


class Parallel2(Parallel):
    def getNextValues(self, state, inp):
        (s1, s2) = state
        (i1, i2) = self.splitValue(inp)
        (newS1, o1) = self.m1.getNextValues(s1, i1)
        (newS2, o2) = self.m2.getNextValues(s2, i2)
        return ((newS1, newS2), (o1, o2))

    def splitValue(self, v):
        if v == 'undefined':
            return ('undefined', 'undefined')
        else:
            return v


class Feedback(SM):
    def __init__(self, sm):
        self.m = sm
        self.start_state = self.m.start_state

    def getNextValues(self, state, inp):
        (_, o) = self.m.getNextValues(state, 'undefined')
        (newS, _) = self.m.getNextValues(state, o)
        return (newS, o)


class Adder(SM):
    def getNextState(self, state, inp):
        (i1, i2) = splitValue(inp)
        return safeAdd(i1, i2)


class Switch(SM):
    def __init__(self, condition, sm1, sm2):
        self.m1 = sm1
        self.m2 = sm2
        self.condition = condition
        self.start_state = (self.m1.start_state, self.m2.start_state)

    def getNextValues(self, state, inp):
        (s1, s2) = state
        if self.condition(inp):
            (ns1, o) = self.m1.getNextValues(s1, inp)
            return ((ns1, s2), o)
        else:
            (ns2,o) = self.m2.getNextValues(s2, inp)
            return ((s1, ns2), o)

class Mux(Switch):
    def getNextValues(self, state, inp):
        (s1, s2) = state
        (ns1, o1) = self.m1.getNextValues(s1, inp)
        (ns2, o2) = self.m2.getNextValues(s2, inp)
        if self.condition(inp):
            return ((ns1, ns2), o1)
        else:
            return ((ns1, ns2), o2)
